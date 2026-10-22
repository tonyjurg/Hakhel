# A local Context Fabric / BHSA investigation

## Table of content (ToC)<a class="anchor" id="TOC"></a>

* <a href="#bullet1">1 - Introduction</a>
* <a href="#bullet2">2 - What is kept locally</a>
* <a href="#bullet3">3 - Two routes to the same BHSA dataset</a>
* <a href="#bullet4">4 - Prepare the environment</a>
* <a href="#bullet5">5 - Start the server and run the notebook</a>
* <a href="#bullet6">6 - Provenance</a>

# 1 - Introduction<a class="anchor" id="bullet1"></a>
##### [Back to ToC](#TOC)

The main item in this directory is
`taf_deuteronomy_31_historical_critical_context_fabric.ipynb`. It investigates
the explicit inclusion of **טף** in Deuteronomy 31:10–13 by means of a local
Context Fabric MCP server and the local ETCBC BHSA 2021 Text-Fabric corpus.

The word *local* is important here. The notebook does not send the biblical
queries to a hosted concordance. Context Fabric opens the BHSA files on this
computer, and the notebook communicates with that server over the loopback
interface. We can therefore keep the corpus version, software, query, and
reported results together in one reproducible environment.

# 2 - What is kept locally<a class="anchor" id="bullet2"></a>
##### [Back to ToC](#TOC)

The following locations are used:

| Item | Location |
|---|---|
| Python environment | `../.context-fabric-venv` |
| BHSA checkout | `data/bhsa` |
| Corpus supplied to MCP | `data/bhsa/tf/2021` |
| MCP endpoint | `http://127.0.0.1:8765/sse` |
| Context Fabric cache | `data/bhsa/tf/2021/.cfm` |
| Context-frame mapping | `context_classification_mapping.json` |
| Classified occurrence table | `results/taf_occurrences_context_classified.csv` |
| Focused classification review | `results/taf_context_classification_review.csv` |

The corpus checkout, compiled cache, virtual environment, PID files, and logs
are intentionally ignored by Git. The notebook and its small research exports
remain suitable for version control.

The context-frame mapping is kept under version control because it is a
researcher-supplied interpretive layer. Context Fabric does not classify a
verse as conflict, movement, provision, or institutional inclusion. The
notebook validates that each of the 42 retrieved references occurs exactly
once before it writes the classified tables.

The four broad frames are accompanied by a narrower description of the event,
the relevant Hebrew phrase, a contextual rendering of `טף`, a close working
translation, and a short reason for the assignment. The English phrases are
reading aids rather than quotations from a published translation. The notebook
also checks that every mapped Hebrew phrase actually occurs in its BHSA verse
after pointing and cantillation are removed.

# 3 - Two routes to the same BHSA dataset<a class="anchor" id="bullet3"></a>
##### [Back to ToC](#TOC)

It is useful to distinguish two ways of “accessing BHSA”:

1. **Direct library/file access.** The Python process running the notebook opens
   the Text-Fabric files and calls the corpus library directly. This gives the
   researcher maximum flexibility, but also ties the analysis closely to that
   particular Python API.
2. **MCP-mediated access.** A separate Context Fabric server opens the same
   files. The notebook uses MCP tools such as `describe_corpus`, `search`, and
   `get_node_features`.

The investigation in this directory uses the second route for all textual
retrieval and linguistic analysis. Direct filesystem access is restricted to
setup and provenance checks, such as confirming the BHSA version directory and
recording its Git commit.

The installed MCP release currently raises an internal `Computeds.sections`
error in its `get_passages` convenience tool. The notebook therefore retrieves
its selected verses with exact `search` templates. This still returns the
actual BHSA verse nodes and text through Context Fabric; it does not introduce
a replacement text or a manually prepared passage table.

MCP transport is yet another matter. A server may communicate over `stdio`,
SSE, or streamable HTTP without changing the corpus which lies behind it. This
notebook uses local SSE because it allows the server to remain loaded while a
series of notebook cells open sessions.

# 4 - Prepare the environment<a class="anchor" id="bullet4"></a>
##### [Back to ToC](#TOC)

The current `cfabric-mcp` release requires Python 3.13. From the repository
root in PowerShell, the complete setup is:

```powershell
winget install --exact --id Python.Python.3.13 --scope user

& "$HOME\AppData\Local\Programs\Python\Python313\python.exe" -m venv .context-fabric-venv
& ".\.context-fabric-venv\Scripts\python.exe" -m pip install -r ".\context_fabric\requirements.txt"

New-Item -ItemType Directory -Force -Path ".\context_fabric\data" | Out-Null
git clone --depth 1 --filter=blob:none --sparse https://github.com/ETCBC/bhsa.git ".\context_fabric\data\bhsa"

Push-Location ".\context_fabric\data\bhsa"
git sparse-checkout set tf/2021
git checkout
Pop-Location
```

# 5 - Start the server and run the notebook<a class="anchor" id="bullet5"></a>
##### [Back to ToC](#TOC)

Start the local server in a separate terminal:

```powershell
& ".\context_fabric\start_local_server.ps1"
```

On the first launch Context Fabric compiles a `.cfm` cache. For the BHSA this
cache is roughly 850 MB; compilation may take several minutes and use several
gigabytes of memory. Later starts can reuse the cache and are considerably
faster.

The notebook also contains a guarded auto-start cell. If port 8765 is already
serving Context Fabric it reuses that process. To execute the complete notebook
from PowerShell, use:

```powershell
& ".\.context-fabric-venv\Scripts\python.exe" `
  ".\context_fabric\run_context_fabric_notebook.py"
```

# 6 - Provenance<a class="anchor" id="bullet6"></a>
##### [Back to ToC](#TOC)

The following resources and versions were used during preparation:

* Context Fabric: <https://github.com/Context-Fabric/context-fabric>
* BHSA: <https://github.com/ETCBC/bhsa>
* BHSA dataset DOI: <https://doi.org/10.17026/dans-z6y-skyh>
* local BHSA commit: `4db00e2157915495e1a4d3d57e41223df24775da`
* BHSA version directory: `tf/2021`

The JSON files below `results/` record the software, corpus, tools, and checks
of the executed notebook. They should be read as a description of that run,
not as a substitute for examining the notebook and the returned passages.
