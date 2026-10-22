# Hakhel and the little ones: a Sefaria reception history

## Table of content (ToC)<a class="anchor" id="TOC"></a>

* <a href="#bullet1">1 - Introduction</a>
* <a href="#bullet2">2 - The reception-historical route</a>
* <a href="#bullet3">3 - Main files</a>
* <a href="#bullet4">4 - Execute the notebook</a>
* <a href="#bullet5">5 - Scope of the evidence</a>

# 1 - Introduction<a class="anchor" id="bullet1"></a>
##### [Back to ToC](#TOC)

This directory studies the reception of Deuteronomy 31:12, and especially the
command to assemble `האנשים והנשים והטף` (“the men, the women, and the little
ones”). The starting question is not whether the children are present—the
biblical verse is quite clear about that—but why they are brought and what
later interpreters believed their presence accomplished.

# 2 - The reception-historical route<a class="anchor" id="bullet2"></a>
##### [Back to ToC](#TOC)

The notebook follows the verse through several stages:

1. the early rabbinic question `טף למה באין?`;
2. medieval biblical commentary and legal codification;
3. early-modern discussions of education, age, merit, and synagogue practice;
4. Hasidic interpretations of spiritual formation and communal solidarity;
5. modern readings of Hakhel as covenant renewal and inclusive education.

These stages are not intended to suggest a simple line of development. The
same rabbinic saying can be reused for different purposes, while later writers
may return directly to the wording of Deuteronomy 31:13 and reopen the question
of what children themselves hear or learn.

# 3 - Main files<a class="anchor" id="bullet3"></a>
##### [Back to ToC](#TOC)

| File | Purpose |
|---|---|
| `hakhel_taf_reception_history.ipynb` | Documented Sefaria MCP retrieval and the reception-historical synthesis |
| `results/reception_evidence.csv` | Curated chronological evidence table |
| `results/search_queries.json` | Hebrew and English search strategy |
| `results/provenance.json` | Endpoint, tools, seed references, and run date |
| `results/audit.json` | Small validation summary |
| `results/consolidated_search_references.csv` | Deduplicated references from the two recorded search runs |
| `results/consolidated_full_texts.csv` | Deduplicated full texts from all recorded Sefaria source runs |
| `results/source_runs/initial_sefaria_mcp/` | Unchanged tables and raw payloads from the earlier exploratory notebook |
| `results/source_runs/targeted_supplement_2026-08-06/` | Public MCP payload and normalized text for the Maor VaShemesh witness |

# 4 - Execute the notebook<a class="anchor" id="bullet4"></a>
##### [Back to ToC](#TOC)

The notebook uses Sefaria's hosted MCP endpoint and requires `mcp`, `pandas`,
`nbformat`, and `tqdm`. Install the recorded environment and open the notebook
from the repository root with:

```powershell
python -m pip install -r ".\reception_history\requirements.txt"
jupyter lab ".\reception_history\hakhel_taf_reception_history.ipynb"
```

The default setting, `RUN_LIVE_RETRIEVAL = False`, rebuilds the derived tables
from the dated source runs already stored in the repository. Change it to
`True` only when a genuinely new live run is intended. Since Sefaria's search
index and available links can change, a new run should receive its own date and
provenance rather than silently replacing the identity of the older evidence.

The final export section normalizes every raw query hit before deduplication,
so repeated hits and all query/reference relationships remain visible. It then
combines the two broad retrievals with the targeted Maor VaShemesh supplement
and produces the deduplicated reading tables. The discovery tags are explicit
keyword rules; the chronological evidence table is a separate researcher-
supplied interpretation layer.

# 5 - Scope of the evidence<a class="anchor" id="bullet5"></a>
##### [Back to ToC](#TOC)

Sefaria is a large but selective digital library. The search results document
the reception represented in Sefaria; they do not amount to a complete
bibliography of Jewish interpretation. Likewise, the dates in the evidence
table are broad scholarly periodizations rather than exact claims about the
composition of each work.

Where textual variants, precise dating, or dependence between sources matter,
the retrieved text should be checked against an appropriate critical edition.
