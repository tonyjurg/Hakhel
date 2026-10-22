# The occurences of טף in the Septuagint

## Table of content (ToC)<a class="anchor" id="TOC"></a>

* <a href="#bullet1">1 - Introduction</a>
* <a href="#bullet2">2 - The two notebooks</a>
* <a href="#bullet3">3 - Running the notebooks</a>
* <a href="#bullet4">4 - From Hebrew references to Greek passages</a>
* <a href="#bullet5">5 - Results and limits</a>

# 1 - Introduction<a class="anchor" id="bullet1"></a>
##### [Back to ToC](#TOC)

This directory adds the Septuagint to the investigation of טף (*ṭaph*) and the Hakhel audience in Deuteronomy 31:10–13. 
The Hebrew notebooks establish the lexical and syntactic evidence first. 
Here the question is how the selected Greek texts represent the little ones or dependants, both in the central covenant passages and across all 42 BHSA occurrences.

Both notebooks use the local [`perseus-mcp`](https://tonyjurg.github.io/Perseus-mcp/) package through an in-process FastMCP client. 
The Greek passages and metadata still come from the Perseus/Scaife services althoug obtained through the MCP tools.

# 2 - The two notebooks<a class="anchor" id="bullet2"></a>
##### [Back to ToC](#TOC)

[`lxx_hakhel_perseus_mcp.ipynb`](lxx_hakhel_perseus_mcp.ipynb) begins with the main passages:

* Deuteronomy 31:10–13, the septennial public reading;
* Deuteronomy 29:10–12, the related covenant assembly; and
* the Greek Joshua parallel to Masoretic Joshua 8:34–35.

[`lxx_taph_42_bhsa_alignment.ipynb`](lxx_taph_42_bhsa_alignment.ipynb) takes the
complete 42-row occurrence table from
[`context_fabric/results/taf_occurrences_context_classified.csv`](../context_fabric/results/taf_occurrences_context_classified.csv).
It maps each BHSA reference to a Greek CTS passage, seeks a small set of
plausible Greek lexical families, and sends uncertain cases to a review queue.

# 3 - Running the notebooks<a class="anchor" id="bullet3"></a>
##### [Back to ToC](#TOC)

From the repository root:

```powershell
python -m pip install -r .\lxx\requirements.txt
jupyter lab .\lxx
```

Both notebooks require network access for the Perseus/Scaife calls. 
The first writes below [`lxx/lxx_hakhel_perseus_results/`](lxx_hakhel_perseus_results); the 42-row alignment writes below [`lxx/lxx_taph_42_alignment_results/`](lxx_taph_42_alignment_results).

The 42-row alignment does not read a SHEBANQ export. Its sole Hebrew input is the Context Fabric table named above. 
The [public SHEBANQ queries](../BHSA_shebanq) serve as an independent control on the BHSA references and word slots; they are not a second or interchangeable alignment input.

# 4 - From Hebrew references to Greek passages<a class="anchor" id="bullet4"></a>
##### [Back to ToC](#TOC)

The Scaife library places the Greek Old Testament under
`urn:cts:greekLit:tlg0527`. The alignment notebook distinguishes three steps:

1. a BHSA book name is mapped to a Scaife work and Greek edition;
2. the Hebrew chapter and verse are mapped to a Greek passage locator; and
3. Greek words in that passage are proposed as possible representatives of טף.

This separation prevents a matching verse number from being mistaken for a finished lexical alignment. 
Two known reference differences are entered explicitly: Hebrew Deuteronomy 29:10 points to Greek 29.11, and Hebrew Joshua 8:35 points to Greek Joshua 9.8. 
Jeremiah is kept under reference review because the Greek and Masoretic arrangements differ substantially.

The Greek candidate list includes such families as `ἀποσκευή`, `ἔκγονον`, `παιδίον` / `παῖς`, `τέκνον`, `νήπιος`, `ἀπαρτία`, and household expressions with `οἶκος` or `πανοικία`. 
The list is explicit and editable. Finding one of these words is a reason to inspect the clause, not a claim that the word is a fixed dictionary equivalent of טף.

# 5 - Results and limits<a class="anchor" id="bullet5"></a>
##### [Back to ToC](#TOC)

These notebooks provide a reproducible route to digital evidence; they do not replace a critical edition or a checked Hebrew–Greek alignment. 
The Perseus text may include apparatus material, and different books present different numbering and textual-history problems.

The 42-row CSV therefore records the Hebrew context, the CTS passage, the Greek text, the candidate tokens, and an alignment status. 
Rows with a failed retrieval, an uncertain reference, no lexical candidate, or several candidates remain visible in a separate review queue.
