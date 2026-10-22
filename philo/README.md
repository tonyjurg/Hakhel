# Philo and Hakhel through Perseus MCP

## Table of content (ToC)<a class="anchor" id="TOC"></a>

* <a href="#bullet1">1 - Introduction</a>
* <a href="#bullet2">2 - The notebook</a>
* <a href="#bullet3">3 - Running the notebook</a>
* <a href="#bullet4">4 - How Perseus MCP is used</a>
* <a href="#bullet5">5 - Recorded results</a>
* <a href="#bullet6">6 - Limits of the search</a>

# 1 - Introduction<a class="anchor" id="bullet1"></a>
##### [Back to ToC](#TOC)

This directory extends the Hakhel investigation from the Septuagint to Philo of Alexandria. 
The question is whether passages in Philo bring together ideas which are important in Deuteronomy 31:10–13: 
a seventh-year setting, the Feast of Booths, public reading or hearing of the law, and the participation of the wider community.

The notebook is a discovery and close-reading aid. A Greek keyword hit points to a passage worth reading; 
it does not by itself show that Philo is discussing Hakhel. The exported CTS URNs keep the route from search result to source text visible.

# 2 - The notebook<a class="anchor" id="bullet2"></a>
##### [Back to ToC](#TOC)

[`philo_hakhel_perseus_mcp.ipynb`](philo_hakhel_perseus_mcp.ipynb) carries out one documented survey of Philo's
Greek corpus using [Perseus-mcp](https://tonyjurg.github.io/Perseus-mcp/). It first checks the available MCP tools and the Scaife library
scope, then searches for several groups of Greek forms connected with booths,
seven, reading, hearing, law, children, women, and men.

Philo's works are restricted by the CTS textgroup `urn:cts:greekLit:tlg0018`. 
The recorded Scaife inventory contains 31 works in that textgroup. 
This scope check matters because the older Perseus CTS inventory and the Scaife library inventory are not identical: 
an author lookup may fail even though the Scaife-backed search contains Philo's texts, so it is not a bug in the perseus-mcp implementation.

# 3 - Running the notebook<a class="anchor" id="bullet3"></a>
##### [Back to ToC](#TOC)

From the repository root:

```powershell
python -m pip install perseus-mcp pandas tqdm
jupyter lab .\philo\philo_hakhel_perseus_mcp.ipynb
```

The notebook requires network access for the Perseus/Scaife calls. A completed
run writes its tables and run summary below
[`philo/philo_hakhel_perseus_results/`](philo_hakhel_perseus_results).

# 4 - How Perseus MCP is used<a class="anchor" id="bullet4"></a>
##### [Back to ToC](#TOC)

The technical route is the same one used in the LXX directory. The notebook imports the local `perseus-mcp` FastMCP server 
and connects to it through an in-process MCP client. 
All corpus operations still pass through `client.call_tool(...)`; 
importing the local server object only avoids the need to launch a separate stdio process for the notebook.

The notebook then follows five steps:

1. It asks the live server for its tool registry and checks the required tools. 
2. It uses `get_scaife_library_metadata` to confirm Philo's textgroup and works.
3. It calls `search_perseus` with Greek Unicode wildcard forms and restricts every query to `urn:cts:greekLit:tlg0018`.
4. It normalizes the returned snippets and CTS passage URNs, then retrieves the full Greek passage with `get_scaife_passage_text`.
5. It keeps the full evidence table, draws out the *De Specialibus Legibus* rows for initial inspection, and records the search plan and audit totals.

This is similar to the LXX notebooks in transport, tool discovery, CTS identification, and passage retrieval. 
The difference lies at the start of the research route. 
The LXX investigation begins with known biblical passages or with the 42 BHSA references. 
The Philo notebook has no fixed Hebrew-to-Greek passage mapping, so it begins with subject-oriented searches and follows their CTS URNs to the Greek text.

# 5 - Recorded results<a class="anchor" id="bullet5"></a>
##### [Back to ToC](#TOC)

The tracked output is kept in [`philo_hakhel_perseus_results/`](philo_hakhel_perseus_results):

| File | Purpose |
|---|---|
| [`philo_hakhel_search_hits.csv`](philo_hakhel_perseus_results/philo_hakhel_search_hits.csv) | Normalized search hits with theme, query, CTS URN, work, reference, and snippet |
| [`philo_hakhel_passage_evidence.csv`](philo_hakhel_perseus_results/philo_hakhel_passage_evidence.csv) | The search evidence joined to the retrieved full Greek passage text |
| [`philo_hakhel_special_laws_focus.csv`](philo_hakhel_perseus_results/philo_hakhel_special_laws_focus.csv) | The smaller set of rows from *De Specialibus Legibus* selected for first inspection |
| [`philo_hakhel_run.json`](philo_hakhel_perseus_results/philo_hakhel_run.json) | Textgroup scope, search terms, paging totals, and audit information for the recorded run |

The present run records nine search terms, 169 themed hits, 151 unique passage URNs, no passage-retrieval failures, and nine focused rows from *De Specialibus Legibus*. 
These figures describe the stored run; a later service or index state may return a different order or count.

# 6 - Limits of the search<a class="anchor" id="bullet6"></a>
##### [Back to ToC](#TOC)

The searches use surface forms rather than treating a zero-result lemma query as evidence of absence. For the Philo dataset, 
form searches return passages where equivalent lemma searches may return none. Wildcards improve recall, but they do not make the survey a complete concordance.

The notebook collects at most two result pages per term. Large reported totals are therefore sampled rather than exhausted.
Search snippets are retained fordiscovery, but interpretation should rest on the full passage text and its CTS URN. 
The Perseus/Scaife text remains a digital reading text and does not replace a critical edition when wording, textual history, or precise citation matters.
