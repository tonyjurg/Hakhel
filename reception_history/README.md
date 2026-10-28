# Hakhel and the little ones: a Sefaria reception history

## Table of contents (ToC)<a class="anchor" id="TOC"></a>

* <a href="#bullet1">1 - Introduction</a>
* <a href="#bullet2">2 - The reception-historical route</a>
* <a href="#bullet3">3 - Main files</a>
* <a href="#bullet4">4 - Execute the notebook</a>
* <a href="#bullet5">5 - Scope of the evidence</a>
* <a href="#bullet6">6 - Sources and reuse</a>

# 1 - Introduction<a class="anchor" id="bullet1"></a>
##### [Back to ToC](#TOC)

This directory studies the reception of Deut 31:12, and especially the command to assemble `האנשים והנשים והטף` (“the men, the women, and the little ones”).
The verse includes the children.
The question here is why they are brought and what later interpreters believed their presence accomplished.

# 2 - The reception-historical route<a class="anchor" id="bullet2"></a>
##### [Back to ToC](#TOC)

The notebook follows the verse through several stages:

1. the early rabbinic question `טף למה באין?`;
2. medieval biblical commentary and legal codification;
3. early-modern discussions of education, age, merit, and synagogue practice;
4. Hasidic interpretations of spiritual formation and communal solidarity;
5. modern readings of Hakhel as covenant renewal and inclusive education.

These stages are not intended to suggest a simple line of development.
The same rabbinic saying can be reused for different purposes, while later writers may return directly to the wording of Deut 31:13 and reopen the question of what children themselves hear or learn.

# 3 - Main files<a class="anchor" id="bullet3"></a>
##### [Back to ToC](#TOC)

| File | Purpose |
|---|---|
| `hakhel_reception.ipynb` | Sefaria MCP retrieval and reception-history synthesis |
| `retrieval_plan.json` | Search queries and reference seeds for the retrieval |
| `results/evidence.csv` | Curated chronological evidence table |
| `results/current_run.json` | Identifies the current run |
| `results/source_runs/live_2026-10-26_105712_58edc937/` | Current run: raw payloads, reading tables, tool inventory, plan, and audit |

# 4 - Execute the notebook<a class="anchor" id="bullet4"></a>
##### [Back to ToC](#TOC)

The notebook uses Sefaria’s hosted MCP endpoint and needs network access.
Its requirements file lists the Python libraries, including the compatible MCP version and timezone data.
Install the recorded environment and open the notebook from the repository root with:

```powershell
python -m pip install -r ".\reception_history\requirements.txt"
jupyter lab ".\reception_history\hakhel_reception.ipynb"
```

The notebook setup pins `mcp==1.30.0` on the compatible 1.x SDK line.

Run all cells to retrieve one fresh run.
`retrieval_plan.json` defines the search queries and the source references to retrieve, including the curated evidence references.
Each execution writes to its own dated folder under `results/source_runs/`.
It retrieves the source texts anew and builds reading tables from that run alone.

The run retrieved on 26 October 2026 uses MCP 1.30.0 and contains 344 successful texts from 345 requests.
Every curated reference has retrieved text.
The audit retains one failed reference: `German Commentary on Mishnah Kiddushin 1:7:7`.
The audit records curated coverage, retrieval errors, and search limits.
The hosted search tool has no pagination parameter; a result-limit warning means discovery may be truncated.

The curated `results/evidence.csv` remains the interpretive layer.
Its categories and readings were prepared with AI assistance and reviewed by the researcher.
Running the retrieval does not rewrite that table.

# 5 - Scope of the evidence<a class="anchor" id="bullet5"></a>
##### [Back to ToC](#TOC)

Sefaria is a large but selective digital library.
The search results document the reception represented in Sefaria; they do not amount to a complete bibliography of Jewish interpretation.
Likewise, the dates in the evidence table are broad scholarly periodizations rather than exact claims about the composition of each work.

Where textual variants, precise dating, or dependence between sources matter, the retrieved text should be checked against an appropriate critical edition.

# 6 - Sources and reuse<a class="anchor" id="bullet6"></a>
##### [Back to ToC](#TOC)

The project’s own code is licensed under the [MIT License](../LICENSE).
Its original research writing and explanatory text are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); see the [text licence](../LICENSE-TEXT.md).
These licences cover the author’s own contributions; source texts and datasets retain their separate terms.

Sefaria text rights differ by version and language.
The stored raw responses retain version titles and source URLs, but do not supply licence fields; the normalized tables do not retain version attribution in each row.
A version-level rights check is still needed before further redistribution of these exports.
See [Sources, attribution, and reuse](../DATA_RIGHTS.md#4---sefaria-texts-and-links) for examples and the separate treatment of links data.
