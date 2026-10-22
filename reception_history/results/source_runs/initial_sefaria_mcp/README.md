# Initial Sefaria MCP discovery run

These files preserve the executed output of the earlier
`sefaria_hakhel_taf_mcp.ipynb` notebook. That notebook was later consolidated
into `reception_history/hakhel_taf_reception_history.ipynb`, but its retrieved
evidence has not been discarded or silently replaced.

The source run used eight searches with a maximum of 25 results per search and
started from Deuteronomy 31:10–13, Chagigah 3a, and Kiddushin 34b. Its query
list remains visible in the raw JSONL file. It is not copied into the later
run's configuration: consolidation joins the two actual recorded runs instead
of pretending that they were executed with one combined search strategy.

| File | Rows | SHA-256 |
|---|---:|---|
| `hakhel_taf_search_refs.csv` | 75 | `B178232F5465DB8D036BC23C13446834A386E342211D1063F79DCCD3D1BEE19E` |
| `hakhel_taf_full_texts.csv` | 78 | `D8679D987E361D4128AF68ED2F948D7AE4EB696B6AE614AF9FC5612529DF054F` |
| `hakhel_taf_raw_search_payloads.jsonl` | 8 payload records | `78A9644AB1355D2C298CA49B7323EA9978434EB15D0398F308459A49FF50496E` |

The hashes record the files at the moment of consolidation. The active
notebook leaves all three files unchanged. It normalizes the 119 individual
query hits from the raw JSONL into the source-history export, uses the full-text
table in the text history, and produces deduplicated reference tables only
after those source rows have been retained. The 75-row search table remains the
earlier notebook's own deduplicated reading table.
