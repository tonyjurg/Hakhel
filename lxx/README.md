# The occurrences of טף in the Septuagint

## Table of contents (ToC)<a class="anchor" id="TOC"></a>

* <a href="#bullet1">1 - Introduction</a>
* <a href="#bullet2">2 - The two notebooks</a>
* <a href="#bullet3">3 - Running the notebooks</a>
* <a href="#bullet4">4 - From Hebrew references to Greek passages</a>
* <a href="#bullet5">5 - Results and limits</a>
* <a href="#bullet6">6 - Sources and reuse</a>

# 1 - Introduction<a class="anchor" id="bullet1"></a>
##### [Back to ToC](#TOC)

This directory adds the Septuagint to the investigation of טף (*ṭap̄*) and the Hakhel audience in Deut 31:10–13.
The Hebrew notebooks establish the lexical and syntactic evidence first.
Here the question is how the selected Greek texts represent the little ones or dependants, both in the central covenant passages and across all 42 BHSA occurrences.

Both notebooks use the local [`perseus-mcp`](https://tonyjurg.github.io/Perseus-mcp/) package through an in-process FastMCP client.
The recorded runs use version 1.0.2 ([DOI](https://doi.org/10.5281/zenodo.20931139)).
A descriptive document on Perseus MCP is available at [doi:10.5281/zenodo.23664266](https://doi.org/10.5281/zenodo.23664266).
The MCP tools retrieve the Greek passages and metadata from the [Perseus/Scaife](https://www.perseus.tufts.edu/hopper) services.

# 2 - The two notebooks<a class="anchor" id="bullet2"></a>
##### [Back to ToC](#TOC)

[`hakhel_lxx.ipynb`](hakhel_lxx.ipynb) begins with the main passages:

* Deut 31:10–13, the septennial public reading;
* Deut 29:10–12, the related covenant assembly; and
* the Greek Joshua parallel to Masoretic Josh 8:34–35.

[`taf_lxx_alignment.ipynb`](taf_lxx_alignment.ipynb) takes the complete 42-row occurrence table from [`context_fabric/results/taf_occurrences.csv`](../context_fabric/results/taf_occurrences.csv).
It maps each BHSA reference to a Greek CTS passage, looks for words from an explicit list of Greek lexical families and places uncertain cases in a review queue.

# 3 - Running the notebooks<a class="anchor" id="bullet3"></a>
##### [Back to ToC](#TOC)

The notebook setup pins `mcp==1.30.0` on the compatible 1.x SDK line.

From the repository root:

```powershell
python -m pip install -r .\lxx\requirements.txt
jupyter lab .\lxx
```

Both notebooks require network access for the Perseus/Scaife calls.
The first writes below [`lxx/lxx_hakhel_perseus_results/`](lxx_hakhel_perseus_results); the 42-row alignment writes below [`lxx/taf_lxx_results/`](taf_lxx_results).

The 42-row alignment does not read a SHEBANQ export.
Its sole Hebrew input is the Context-Fabric table named above.
The [public SHEBANQ queries](../SHEBANQ-BHSA/shebanq_controls.ipynb) serve as an independent control on the BHSA references and word slots; they are not a second or interchangeable alignment input.

# 4 - From Hebrew references to Greek passages<a class="anchor" id="bullet4"></a>
##### [Back to ToC](#TOC)

The Scaife library places the Greek Old Testament under `urn:cts:greekLit:tlg0527`.
The alignment notebook distinguishes three steps:

1. a BHSA book name is mapped to a Scaife work and Greek edition;
2. the Hebrew chapter and verse are mapped to a Greek passage locator; and
3. Greek words in that passage are proposed as possible representatives of טף.

This separation prevents a matching verse number from being mistaken for a finished lexical alignment.
Two known reference differences are entered explicitly: Hebrew Deut 29:10 points to Greek 29.11, and Hebrew Josh 8:35 points to Greek Josh 9.8.
Jeremiah is kept under reference review because the Greek and Masoretic arrangements differ substantially.

The Greek candidate list includes such families as `ἀποσκευή`, `ἔκγονον`, `παιδίον` / `παῖς`, `τέκνον`, `νήπιος`, `ἀπαρτία`, and household expressions with `οἶκος` or `πανοικία`.
The list is explicit and editable.
Finding one of these words is a reason to inspect the clause, not a claim that the word is a fixed dictionary equivalent of טף.

# 5 - Results and limits<a class="anchor" id="bullet5"></a>
##### [Back to ToC](#TOC)

Each new execution writes `run_timing.json` beside its result tables.
The main provenance export also includes `run_id`, `started_at_utc`, `completed_at_utc`, retrieval dates in UTC, software versions, source editions, and retrieval endpoints.
The request log records start and end times even when a request fails.
These timestamps describe MCP calls during the run, including possible cached responses; they are not upstream publication dates.
Each execution writes the named result files.
The recorded retrieval date is 26 October 2026 (UTC).
During the alignment run, the Perseus CTS catalogue returned HTTP 503; the notebook validated all 12 selected editions through Scaife metadata instead and recorded that fallback in `alignment_mapping_provenance.json`.

These notebooks record how the digital passages were retrieved and compared.
The proposed Hebrew–Greek alignments still need to be checked against their clauses and, where needed, a critical edition.
The Perseus text may include apparatus material, and different books present different numbering and textual-history problems.

The 42-row CSV therefore records the Hebrew context, the CTS passage, the Greek text, the candidate tokens, and an alignment status.
Rows with a failed retrieval, an uncertain reference, no lexical candidate, or several candidates remain visible in a separate review file.

# 6 - Sources and reuse<a class="anchor" id="bullet6"></a>
##### [Back to ToC](#TOC)

The project’s own code is licensed under the [MIT License](../LICENSE).
Its original research writing and explanatory text are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); see the [text licence](../LICENSE-TEXT.md).
These licences cover the author’s own contributions; source texts and datasets retain their separate terms.

The alignment tables combine BHSA material with Greek digital editions.
BHSA data is CC BY-NC 4.0, while the checked [First1KGreek](https://opengreekandlatin.github.io/First1KGreek/) editions are CC BY-SA 4.0.
Keep their credits and terms separate when reusing a combined table.
See [Sources, attribution, and reuse](../DATA_RIGHTS.md) for edition checks and attribution details.
