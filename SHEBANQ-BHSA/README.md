# SHEBANQ controls for the Hakhel investigation

## Table of contents (ToC)<a class="anchor" id="TOC"></a>

* <a href="#bullet1">1 - Purpose</a>
* <a href="#bullet2">2 - The public queries</a>
* <a href="#bullet3">3 - Running the notebook</a>
* <a href="#bullet4">4 - Outputs and checks</a>
* <a href="#bullet5">5 - Reading the results</a>
* <a href="#bullet6">6 - Sources and reuse</a>

# 1 - Purpose<a class="anchor" id="bullet1"></a>
##### [Back to ToC](#TOC)

[`shebanq_controls.ipynb`](shebanq_controls.ipynb) reads five public SHEBANQ query records for BHSA 2021.
These provide a separate route for checking the occurrences of טף and combinations of the audience terms in Deut 31:12.

The main check compares the all-טף query with the 42 word slots and references exported by the [Context-Fabric notebook](../context_fabric/hakhel_bhsa.ipynb).
Both routes use BHSA 2021.
Agreement checks the retrieval and reference mapping; it does not provide a second textual witness or confirm the contextual classifications.

# 2 - The public queries<a class="anchor" id="bullet2"></a>
##### [Back to ToC](#TOC)

The query IDs and local descriptions are listed in [`public_shebanq_queries.json`](public_shebanq_queries.json).

| Query ID | What it checks |
|---|---|
| 7334 | All 42 occurrences of טף; compared with the Context-Fabric export. |
| 7333 | Verses with טף and at least one of אישׁ, אשׁה, or גר. |
| 7328 | Verses with טף together with אישׁ, אשׁה, and גר. |
| 7329 | Verses with אישׁ, אשׁה, and גר but without טף; a negative control. |
| 7335 | Verses with both גר and טף. |

The notebook reads the stored query metadata and recorded result CSVs through public HTTP endpoints.
It does not submit new MQL queries for execution.
It retains the MQL returned by SHEBANQ so the results can be read alongside the query that produced them.

No account, password, or browser login is required.
Shared access and formal publication status are recorded separately.
The notebook checks that the records are shared and that their BHSA 2021 executions have status `good`.

# 3 - Running the notebook<a class="anchor" id="bullet3"></a>
##### [Back to ToC](#TOC)

First run the Context-Fabric notebook if its comparison input is missing:

`context_fabric/results/taf_occurrences.csv`

Then, from the repository root, install the libraries and open Jupyter in this directory:

```powershell
python -m pip install -r ".\SHEBANQ-BHSA\requirements.txt"
Set-Location ".\SHEBANQ-BHSA"
jupyter lab "shebanq_controls.ipynb"
```

Start the notebook kernel in `SHEBANQ-BHSA`; its paths are relative to that working directory.
Run the cells in order.
Network access is needed for the SHEBANQ requests.
The local Context-Fabric server does not need to be running for this comparison, because the notebook reads its exported CSV.

# 4 - Outputs and checks<a class="anchor" id="bullet4"></a>
##### [Back to ToC](#TOC)

The notebook writes to `results/public_query_control/`.
Rerunning it replaces files with the same names.

| Output | Purpose |
|---|---|
| `query_results/` | One prepared CSV for each successfully retrieved query. |
| `query_details.csv` | Query metadata, counts, MQL, and retrieval status. |
| `shebanq_query_details.json` | Metadata with the retrieval time, access notes, and book-name mapping. |
| `controls.csv` | The prepared result rows from the retrieved queries. |
| `bhsa_comparison.csv` | Comparison by word slot, including references from both routes. |
| `control_audit.json` | Summary written after the final checks pass. |

The final checks require 42 rows in the all-טף control and agreement with all 42 Context-Fabric word slots and mapped references.
They also require the negative control to be empty.
A failed check stops execution and should be examined before using the results.

# 5 - Reading the results<a class="anchor" id="bullet5"></a>
##### [Back to ToC](#TOC)

SHEBANQ result counts and exported focus-row counts describe different aspects of a query.
Read them together with the returned MQL.
A query that focuses on several objects can return more rows than a simple count of verses suggests.

Book names are mapped explicitly before references are compared.
The word-slot comparison is the main control; a matching number of rows alone would not show that the two routes found the same occurrences.

The audience queries locate combinations of words within a verse.
Their results need to be read in context before drawing conclusions about who participates, how the terms relate, or what a passage means.
The controls support the Hebrew investigation; they do not replace close reading.

# 6 - Sources and reuse<a class="anchor" id="bullet6"></a>
##### [Back to ToC](#TOC)

The project’s own code is licensed under the [MIT License](../LICENSE).
Its original research writing and explanatory text are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); see the [text licence](../LICENSE-TEXT.md).
These licences cover the author’s own contributions; source texts and datasets retain their separate terms.

The BHSA data behind these controls is CC BY-NC 4.0.
Keep query authors and query IDs alongside their MQL and descriptions; public access does not establish a blanket reuse licence for those contributions.
See [Sources, attribution, and reuse](../DATA_RIGHTS.md#2---bhsa-and-the-shebanq-controls).
