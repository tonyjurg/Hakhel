# A local Context-Fabric / BHSA investigation

## Table of contents (ToC)<a class="anchor" id="TOC"></a>

* <a href="#bullet1">1 - Introduction</a>
* <a href="#bullet2">2 - What is kept locally</a>
* <a href="#bullet3">3 - Two routes to the same BHSA dataset</a>
* <a href="#bullet4">4 - Prepare the environment</a>
* <a href="#bullet5">5 - Start the server and run the notebook</a>
* <a href="#bullet6">6 - Provenance</a>
* <a href="#bullet7">7 - Sources and reuse</a>

# 1 - Introduction<a class="anchor" id="bullet1"></a>
##### [Back to ToC](#TOC)

The main item in this directory is `hakhel_bhsa.ipynb`.
It investigates the explicit inclusion of **טף** in Deut 31:10–13 by means of a local Context-Fabric MCP server and the local ETCBC BHSA 2021 Text-Fabric corpus.

Context-Fabric opens the BHSA files on the local computer.
The notebook sends its queries to the local server at `127.0.0.1`.
We can therefore keep the corpus version, software, query, and reported results together in one reproducible environment.

# 2 - What is kept locally<a class="anchor" id="bullet2"></a>
##### [Back to ToC](#TOC)

The following locations are used:

| Item | Location |
|---|---|
| Default Python environment | `%USERPROFILE%\anaconda3\envs\context_fabric` |
| BHSA checkout | `data/bhsa` |
| Corpus supplied to MCP | `data/bhsa/tf/2021` |
| MCP endpoint | `http://127.0.0.1:8765/sse` |
| Context-Fabric cache | `data/bhsa/tf/2021/.cfm` |
| Context-frame mapping | `context_classification_mapping.json` |
| Classified occurrence table | `results/taf_occurrences.csv` |
| Focused classification review | `results/context_review.csv` |

The corpus checkout, compiled cache, virtual environment, PID files, and logs are intentionally ignored by Git.
The notebook and its small research exports remain suitable for version control.

The context-frame mapping is kept under version control because it is a researcher-supplied interpretive layer.
Context-Fabric does not classify a verse as conflict, movement, provision, or institutional inclusion.
The notebook validates that each of the 42 retrieved references occurs exactly once before it writes the classified tables.

The four broad frames are accompanied by a narrower description of the event, the relevant Hebrew phrase, a contextual rendering of `טף`, a close working translation, and a short reason for the assignment.
The English phrases are reading aids rather than quotations from a published translation.
The notebook also checks that every mapped Hebrew phrase actually occurs in its BHSA verse after pointing and cantillation are removed.

# 3 - Two routes to the same BHSA dataset<a class="anchor" id="bullet3"></a>
##### [Back to ToC](#TOC)

It is useful to distinguish two ways of “accessing BHSA”:

1. **Direct library/file access.** The Python process running the notebook opens the Text-Fabric files and calls the corpus library directly.
This gives the researcher maximum flexibility, but also ties the analysis closely to that particular Python API.
2. **MCP-mediated access.** A separate Context-Fabric server opens the same files.
The notebook uses MCP tools such as `describe_corpus`, `search`, and `get_node_features`.

The investigation in this directory uses the second route for all textual retrieval and linguistic analysis.
Direct filesystem access is restricted to setup and provenance checks, such as confirming the BHSA version directory and recording its Git commit.

The recorded setup raised an internal `Computeds.sections` error in its `get_passages` convenience tool.
The notebook therefore retrieves its selected verses with exact `search` templates.
This still returns the actual BHSA verse nodes and text through Context-Fabric; it does not introduce a replacement text or a manually prepared passage table.

MCP transport is yet another matter.
A server may communicate over `stdio`, SSE, or streamable HTTP without changing the corpus which lies behind it.
This notebook uses local SSE because it allows the server to remain loaded while a series of notebook cells open sessions.

# 4 - Prepare the environment<a class="anchor" id="bullet4"></a>
##### [Back to ToC](#TOC)

The pinned `cfabric-mcp==0.1.7` package requires Python 3.13 or later and MCP below version 2.
The recorded run uses Python 3.14.2 and `mcp==1.30.0`.
From an Anaconda PowerShell prompt at the repository root:

```powershell
# Create this environment only if it does not already exist.
conda create -n context_fabric python=3.14
conda activate context_fabric
python -m pip install -r ".\context_fabric\requirements.txt"
```

If the local BHSA checkout is missing, follow [Obtain BHSA 2021](../REPRODUCING.md#bullet3).
Those instructions select the corpus commit used by the recorded run, rather than the current default branch.

# 5 - Start the server and run the notebook<a class="anchor" id="bullet5"></a>
##### [Back to ToC](#TOC)

The startup script uses the Anaconda environment at `$env:USERPROFILE\anaconda3\envs\context_fabric\python.exe` by default.
Start it from the repository root in a separate terminal:

```powershell
& ".\context_fabric\start_local_server.ps1"
```

For an environment in another location, pass its Python path with `-Python`.
The notebook has a separate override, `CONTEXT_FABRIC_PYTHON`; set that environment variable before starting Jupyter when using a different location.
Both should point to the same working environment.
The notebook also accepts `CONTEXT_FABRIC_PORT` when a port other than 8765 is needed; use the same value with the launcher’s `-Port` option.

On the first launch Context-Fabric compiles a `.cfm` cache.
Compilation can take several minutes and use several gigabytes of memory.
Later starts can reuse the cache and are considerably faster.

The notebook also contains a guarded auto-start cell.
It reuses a service already listening on the configured port; the later MCP checks confirm that the required tools are available.
To execute the complete notebook from PowerShell, use:

```powershell
& "$env:USERPROFILE\anaconda3\envs\context_fabric\python.exe" `
  ".\context_fabric\run_context_fabric_notebook.py"
```

# 6 - Provenance<a class="anchor" id="bullet6"></a>
##### [Back to ToC](#TOC)

The following resources and versions were used during preparation:

Context-Fabric is described in Cody Kingham’s [“Carrying Text-Fabric Forward: Context-Fabric and the Scalable Corpus Ecosystem”](https://github.com/Context-Fabric/context-fabric/blob/master/docs/intro-to-cf/intro-to-cf.pdf) (January 2026).
The recorded environment uses `context-fabric==0.5.7` and `cfabric-mcp==0.1.7`.

* Context-Fabric: <https://github.com/Context-Fabric/context-fabric>
* BHSA: <https://github.com/ETCBC/bhsa>
* BHSA dataset DOI: <https://doi.org/10.17026/dans-z6y-skyh>
* local BHSA commit: `4db00e2157915495e1a4d3d57e41223df24775da`
* BHSA version directory: `tf/2021`

The command-line wrapper executes the notebook with the registered `python3` kernel.
Make sure that kernel has the notebook dependencies installed.

The JSON files below `results/` record the software, corpus, tools, and checks of the executed notebook.
They should be read as a description of that run, not as a substitute for examining the notebook and the returned passages.

# 7 - Sources and reuse<a class="anchor" id="bullet7"></a>
##### [Back to ToC](#TOC)

The project’s own code is licensed under the [MIT License](../LICENSE).
Its original research writing and explanatory text are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); see the [text licence](../LICENSE-TEXT.md).
These licences cover the author’s own contributions; source texts and datasets retain their separate terms.

BHSA 2021 data is supplied under CC BY-NC 4.0, separately from software licences.
Credit ETCBC and retain the dataset DOI and applicable notices when sharing reproduced data.
See [Sources, attribution, and reuse](../DATA_RIGHTS.md#2---bhsa-and-the-shebanq-controls) for details.
