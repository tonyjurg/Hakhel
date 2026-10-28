"""UTC execution and MCP-request records for the Greek research notebooks."""

from datetime import datetime, timezone
from importlib import metadata
import json
import os
from pathlib import Path
import platform
import time
from uuid import uuid4


def _utc_now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


class RunProvenance:
    def __init__(self, route, output_dir, server):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.record = {
            "run_id": f"{route}_{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}_{uuid4().hex[:8]}",
            "started_at_utc": _utc_now(),
            "completed_at_utc": None,
            "status": "running",
            "software_versions": {"python": platform.python_version()},
            "retrieval_endpoints": {
                name: getattr(server, name, None)
                for name in ("CTS_BASE", "SCAIFE_SEARCH", "SCAIFE_LIBRARY")
            },
            "source_editions": [],
            "source_retrieval_started_at_utc": None,
            "source_retrieval_completed_at_utc": None,
            "retrieval_dates_utc": [],
            "cache_environment": {
                name: os.environ.get(name)
                for name in ("PERSEUS_MCP_DISABLE_CACHE", "PERSEUS_MCP_CACHE_DIR", "PERSEUS_MCP_CACHE_TTL_SECONDS")
            },
            "timestamp_scope": "Notebook execution and MCP calls; a tool may serve cached upstream data. These are not upstream publication or revision dates.",
            "retrieval_requests": [],
        }
        for package in ("perseus-mcp", "fastmcp", "mcp", "pandas"):
            try:
                self.record["software_versions"][package] = metadata.version(package)
            except metadata.PackageNotFoundError:
                self.record["software_versions"][package] = None
        self._save()

    def _save(self):
        path = self.output_dir / "run_timing.json"
        temporary = path.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(self.record, ensure_ascii=False, indent=2), encoding="utf-8")
        # Windows sync/indexing processes can briefly hold the previous file.
        # Retry replacement rather than turning a completed tool call into a
        # spurious source-retrieval failure.
        for attempt in range(6):
            try:
                temporary.replace(path)
                break
            except PermissionError:
                if attempt == 5:
                    raise
                time.sleep(0.05 * (2 ** attempt))

    async def call_tool(self, client, name, arguments):
        request = {
            "tool": name,
            "arguments": arguments,
            "started_at_utc": _utc_now(),
            "completed_at_utc": None,
            "status": "running",
        }
        self.record["retrieval_requests"].append(request)
        if self.record["source_retrieval_started_at_utc"] is None:
            self.record["source_retrieval_started_at_utc"] = request["started_at_utc"]
        self._save()
        try:
            result = await client.call_tool(name, arguments)
            request["status"] = "tool_error" if (
                getattr(result, "isError", False) or getattr(result, "is_error", False)
            ) else "returned"
            return result
        except BaseException as exc:
            request["status"] = "error"
            request["error"] = f"{type(exc).__name__}: {exc}"
            raise
        finally:
            request["completed_at_utc"] = _utc_now()
            self.record["source_retrieval_completed_at_utc"] = request["completed_at_utc"]
            self.record["retrieval_dates_utc"] = sorted({
                value[:10]
                for item in self.record["retrieval_requests"]
                for key in ("started_at_utc", "completed_at_utc")
                if (value := item.get(key))
            })
            self._save()

    def finish(self, source_editions):
        self.record["source_editions"] = sorted(set(source_editions))
        self.record["completed_at_utc"] = _utc_now()
        self.record["status"] = "completed"
        self._save()
        # Returned/tool-error counts are transport observations; corpus-specific
        # audits still determine whether the returned payloads are usable.
        return dict(self.record)
