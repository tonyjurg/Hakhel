# Philo and Hakhel through Perseus MCP

## Table of contents (ToC)<a class="anchor" id="TOC"></a>

* <a href="#bullet1">1 - Introduction</a>
* <a href="#bullet2">2 - The notebook</a>
* <a href="#bullet3">3 - Running the notebook</a>
* <a href="#bullet4">4 - How Perseus MCP is used</a>
* <a href="#bullet5">5 - Recorded results</a>
* <a href="#bullet6">6 - Limits of the search</a>
* <a href="#bullet7">7 - Sources and reuse</a>

# 1 - Introduction<a class="anchor" id="bullet1"></a>
##### [Back to ToC](#TOC)

This directory extends the Hakhel investigation from the Septuagint to Philo of Alexandria.
The question is whether passages in Philo bring together ideas which are important in Deut 31:10–13: a seventh-year setting, the Feast of Booths, public reading or hearing of the law, and the participation of the wider community.

The notebook is a discovery and close-reading aid.
A Greek keyword hit points to a passage worth reading; it does not by itself show that Philo is discussing Hakhel.
The exported CTS URNs keep the route from search result to source text visible.

# 2 - The notebook<a class="anchor" id="bullet2"></a>
##### [Back to ToC](#TOC)

[`hakhel_philo.ipynb`](hakhel_philo.ipynb) carries out one documented survey of Philo's Greek texts available through [Perseus-mcp](https://tonyjurg.github.io/Perseus-mcp/).
The recorded runs use version 1.0.2 ([DOI](https://doi.org/10.5281/zenodo.20931139)).
A descriptive document on Perseus MCP is available at [doi:10.5281/zenodo.23664266](https://doi.org/10.5281/zenodo.23664266).
It first checks the available MCP tools and the Scaife library scope, then searches for several groups of Greek forms connected with booths, seven, reading, hearing, law, children, women, and men.

Philo's works are restricted by the CTS textgroup `urn:cts:greekLit:tlg0018`.
The recorded Scaife inventory contains 31 works in that textgroup.
This scope check matters because the older Perseus CTS inventory and the Scaife library inventory are not identical: an author lookup may fail even though the Scaife-backed search contains Philo's texts, so an empty author lookup alone does not establish that the texts are unavailable.

# 3 - Running the notebook<a class="anchor" id="bullet3"></a>
##### [Back to ToC](#TOC)

The notebook setup pins `mcp==1.30.0` on the compatible 1.x SDK line.

From the repository root:

```powershell
python -m pip install -r ".\philo\requirements.txt"
jupyter lab .\philo\hakhel_philo.ipynb
```

The notebook requires network access for the Perseus/Scaife calls.
The output path is relative to the kernel’s working directory.
Start the kernel in `philo` to write the tables and run summary below [`philo/philo_hakhel_perseus_results/`](philo_hakhel_perseus_results).

# 4 - How Perseus MCP is used<a class="anchor" id="bullet4"></a>
##### [Back to ToC](#TOC)

The technical route is the same one used in the LXX directory.
The notebook imports the local `perseus-mcp` FastMCP server and connects to it through an in-process MCP client.
All corpus operations still pass through `client.call_tool(...)`; importing the local server object only avoids the need to launch a separate stdio process for the notebook.

The notebook then follows five steps:

1. It asks the live server for its tool registry and checks the required tools.
2. It uses `get_scaife_library_metadata` to confirm Philo's textgroup and works.
3. It calls `search_perseus` with Greek Unicode wildcard forms and restricts every query to `urn:cts:greekLit:tlg0018`.
4. It normalizes the returned snippets and CTS passage URNs, then retrieves the full Greek passage with `get_scaife_passage_text`.
5. It keeps the full evidence table, draws out the *De specialibus legibus* rows for initial inspection, and records the search plan and audit totals.

This is similar to the LXX notebooks in transport, tool discovery, CTS identification, and passage retrieval.
The difference lies at the start of the research route.
The LXX investigation begins with known biblical passages or with the 42 BHSA references.
The Philo notebook has no fixed Hebrew-to-Greek passage mapping, so it begins with subject-oriented searches and follows their CTS URNs to the Greek text.

# 5 - Recorded results<a class="anchor" id="bullet5"></a>
##### [Back to ToC](#TOC)

Each new execution writes `run_timing.json` beside its result tables.
The main provenance export also includes `run_id`, `started_at_utc`, `completed_at_utc`, retrieval dates in UTC, software versions, source editions, and retrieval endpoints.
The request log records start and end times even when a request fails.
These timestamps describe MCP calls during the run, including possible cached responses; they are not upstream publication dates.
Each execution writes the named result files.

The tracked output is kept in [`philo_hakhel_perseus_results/`](philo_hakhel_perseus_results):

| File | Purpose |
|---|---|
| [`search_hits.csv`](philo_hakhel_perseus_results/search_hits.csv) | Normalized search hits with theme, query, CTS URN, work, reference, and snippet |
| [`passages.csv`](philo_hakhel_perseus_results/passages.csv) | The search evidence joined to the retrieved full Greek passage text |
| [`special_laws.csv`](philo_hakhel_perseus_results/special_laws.csv) | The smaller set of rows from *De specialibus legibus* selected for first inspection |
| [`philo_hakhel_run.json`](philo_hakhel_perseus_results/philo_hakhel_run.json) | Textgroup scope, search terms, paging totals, and audit information for the recorded run |

The run retrieved on 26 October 2026 (UTC) records nine search terms, 169 themed hits, 151 unique passage URNs, no passage-retrieval failures, and nine focused rows from *De specialibus legibus*.
These figures describe the stored run; a later service or index state may return a different order or count.

# 6 - Limits of the search<a class="anchor" id="bullet6"></a>
##### [Back to ToC](#TOC)

The searches use surface forms rather than treating a zero-result lemma query as evidence of absence.
The recorded run uses form searches; it does not establish the coverage of the lemma index.
Wildcards improve recall, but they do not make the survey a complete concordance.

The notebook collects at most two result pages per term.
Large reported totals are therefore sampled rather than exhausted.
Search snippets are retained for discovery, but interpretation should rest on the full passage text and its CTS URN.
The Perseus/Scaife text remains a digital reading text and does not replace a critical edition when wording, textual history, or precise citation matters.

# 7 - Sources and reuse<a class="anchor" id="bullet7"></a>
##### [Back to ToC](#TOC)

The project’s own code is licensed under the [MIT License](../LICENSE).
Its original research writing and explanatory text are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); see the [text licence](../LICENSE-TEXT.md).
These licences cover the author’s own contributions; source texts and datasets retain their separate terms.

The checked First1KGreek edition of Philo’s De vita Mosis identifies CC BY-SA 4.0.
Retain the CTS identifiers and credit the print editor and digital edition contributors; check the header for each edition being reused.
See [Sources, attribution, and reuse](../DATA_RIGHTS.md#3---greek-editions-through-perseus-and-scaife) for the source notice and remaining checks.
