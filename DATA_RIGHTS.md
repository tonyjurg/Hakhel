# Sources, attribution, and reuse

These notes distinguish the project's own work from material retrieved from other sources.
The third-party source statements were checked on 23 October 2026; they are not a complete rights clearance for every exported passage.
Public access through an API or MCP tool does not by itself establish permission to redistribute its contents.

## 1 - Project code and research writing

The project's original code, including notebook code cells, is licensed under the [MIT License](LICENSE).
Its original research writing and explanatory text, including README files and notebook prose, are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); see the [text licence](LICENSE-TEXT.md).
Credit Tony Jurg when reusing the original text, link the licence and repository, and indicate any changes.

These grants cover the author's own contributions, not quoted source material, retrieved passages, datasets, or third-party code.
The licences of installed tools apply to those tools and do not automatically apply to the texts they retrieve.
The source terms below remain separate from the project licences.

## 2 - BHSA and the SHEBANQ controls

The [BHSA data licence statement](https://github.com/ETCBC/bhsa#license) identifies the dataset as [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).
It asks users to credit the Eep Talstra Centre for Bible and Computer, VU University Amsterdam, and cite [the dataset DOI](https://doi.org/10.17026/dans-z6y-skyh).
It directs requests for commercial use to the German Bible Society.
The MIT file in the BHSA repository must not be treated as a replacement for that separate data statement.

This affects BHSA text and linguistic data reproduced in Context-Fabric exports, SHEBANQ result tables, and the Hebrew columns of the LXX alignment tables.
Retain the dataset attribution, version (BHSA 2021), licence link, and a description of changes when sharing these materials under the data licence.
A mixed Hebrew–Greek table cannot be described as unrestricted simply because one component permits commercial reuse.

## 3 - Greek editions through Perseus and Scaife

The notebooks use edition identifiers ending in `1st1K-grc1` from [First1KGreek](https://github.com/OpenGreekAndLatin/First1KGreek).
That collection supplies a [CC BY-SA 4.0 licence](https://github.com/OpenGreekAndLatin/First1KGreek/blob/master/license.md).
The checked TEI headers for [Deuteronomy, edited by Henry Barclay Swete](https://github.com/OpenGreekAndLatin/First1KGreek/blob/master/data/tlg0527/tlg005/tlg0527.tlg005.1st1K-grc1.xml) and [Philo's De vita Mosis, edited by Leopold Cohn](https://github.com/OpenGreekAndLatin/First1KGreek/blob/master/data/tlg0018/tlg022/tlg0018.tlg022.1st1K-grc1.xml) also identify CC BY-SA 4.0 and credit the digital edition's contributors.
These are checked examples, not a passage-by-passage verification of every edition in the exports.

For reused Greek passages, retain the author, work, editor, edition and CTS URN, credit the digital source and its contributors, link the applicable licence, and identify changes such as markup removal.
ShareAlike applies to shared adaptations within the licence's scope; it does not automatically license every independent item in this repository.
Check the specific edition header for any additional attribution information or differing terms.
The age of an ancient work alone does not establish the status of its digital edition, apparatus, or modern translation.

## 4 - Sefaria texts and links

[Sefaria's copyright guidance](https://developers.sefaria.org/docs/usage-of-our-name-and-logo) distinguishes the licence of each text version and language from the terms for its links dataset.
Text versions may be public domain or have different Creative Commons terms; a missing licence is not confirmation that a text is unrestricted.
Its links dataset is described as CC BY, requiring attribution; the guidance does not specify the licence version there.
Text embedded in a link response still needs its own version check.

The recorded reception-history run stores version titles and source URLs in `raw_full_text_payloads.jsonl`, but the returned version objects do not include licence fields.
The normalized CSVs select Hebrew and English text without carrying those version details into each row.
Those CSVs, saved notebook outputs, search snippets, and raw payloads therefore need version-level attribution and rights checks before further redistribution.
No single licence is asserted for the complete reception-history export.

For example, the saved responses include THE JPS TANAKH: Gender-Sensitive Edition and Miqra according to the Masorah.
[Sefaria's sources page](https://lite.sefaria.org/sources-and-licenses) lists these as CC BY-NC and CC BY-SA respectively, without specifying licence versions on that page.
Confirm the exact edition's notice rather than extending those labels to every Sefaria text.
