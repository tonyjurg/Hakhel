# Reproducing the Hakhel notebooks

This guide explains how to recreate the software setup and run the research workflow from a fresh clone.
You do not need the author's virtual environments, Anaconda folders, caches, or logs.
The notebooks, configuration files, curated inputs, and recorded results in the repository are the starting point.

Rerunning the method and obtaining identical files are different things.
BHSA can be fixed to the recorded source commit, but Sefaria, SHEBANQ, and Perseus/Scaife are online services whose responses may change.
Keep the recorded results when comparing a new execution with the published run.

## Table of contents (ToC)<a class="anchor" id="TOC"></a>

* <a href="#bullet1">1 - What you need</a>
* <a href="#bullet2">2 - Create the Python environments</a>
* <a href="#bullet3">3 - Obtain BHSA 2021</a>
* <a href="#bullet4">4 - Run the notebooks in order</a>
* <a href="#bullet5">5 - Check and record the results</a>
* <a href="#bullet6">6 - Common problems and current limits</a>

# 1 - What you need<a class="anchor" id="bullet1"></a>
##### [Back to ToC](#TOC)

The commands below use Windows PowerShell with Git and Conda available.
They describe the current Windows setup; other systems need different Python executable paths and a replacement for the PowerShell server launcher.
Network access is needed to install packages, download BHSA, and contact the hosted text services.
The notebook routes described here do not require account credentials.

Clone the repository and enter it:

```powershell
git clone https://github.com/tonyjurg/Hakhel.git
Set-Location Hakhel
git rev-parse HEAD
```

Record that commit ID with your results.
If you already have a clone, keep a separate copy of the recorded results before rerunning notebooks that overwrite their output files.
Do not copy `.context-fabric-venv/` from another computer; its paths and installed binaries are specific to the original installation.

Keep these authored inputs:

| Input | Role |
|---|---|
| `context_fabric/context_classification_mapping.json` | Context frames, selected phrases, working translations, and interpretation notes. |
| `SHEBANQ-BHSA/public_shebanq_queries.json` | The five public query IDs and their local descriptions. |
| `reception_history/retrieval_plan.json` | Search terms and reference seeds for a fresh Sefaria run. |
| `reception_history/results/evidence.csv` | The curated chronological interpretation table. |

These files contain choices that a new source retrieval cannot reconstruct.
The LXX reference overrides and Greek candidate families are defined in its notebooks and must also be retained.
See [DATA_RIGHTS.md](DATA_RIGHTS.md) before redistributing source texts or combined tables.

# 2 - Create the Python environments<a class="anchor" id="bullet2"></a>
##### [Back to ToC](#TOC)

Use separate environments for the four routes below.
All MCP routes pin SDK version 1.30.0; their remaining dependencies and Python requirements are kept separate.
The Perseus notebooks also have their own dependency set.
The MCP 1.30.0 pin includes the session-retention fix in [GHSA-84m7-p3x7-pcfv](https://github.com/modelcontextprotocol/python-sdk/security/advisories/GHSA-84m7-p3x7-pcfv).
That advisory concerns stateful Streamable HTTP servers; the notebook routes here use local SSE, a hosted SSE client, or an in-process client.
Run the installation commands from the repository root in an Anaconda PowerShell prompt.
Create each environment only once.

**Context-Fabric**

```powershell
conda create -n hakhel-context python=3.14 -y
conda activate hakhel-context
python -m pip install -r ".\context_fabric\requirements.txt"
python -m pip install jupyterlab
python -m ipykernel install --user --name hakhel-context --display-name "Hakhel - Context Fabric"
python -m pip check
```

Tell both the notebook and the server launcher which Python to use:

```powershell
$env:CONTEXT_FABRIC_PYTHON = (Get-Command python).Source
```

Set this after activating `hakhel-context`, in the same terminal from which you will launch Jupyter.
It overrides the notebook's default path to the author's Anaconda environment.
The variable is not a credential and only lasts for this PowerShell session.

**SHEBANQ**

```powershell
conda create -n hakhel-shebanq python=3.13 -y
conda activate hakhel-shebanq
python -m pip install -r ".\SHEBANQ-BHSA\requirements.txt"
python -m pip install ipykernel
python -m ipykernel install --user --name hakhel-shebanq --display-name "Hakhel - SHEBANQ"
python -m pip check
```

**Septuagint and Philo**

```powershell
conda create -n hakhel-greek python=3.13 -y
conda activate hakhel-greek
python -m pip install -r ".\philo\requirements.txt"
python -m pip install ipykernel
python -m ipykernel install --user --name hakhel-greek --display-name "Hakhel - Greek texts"
python -m pip check
```

The Philo requirements include the LXX requirements and add `tqdm`.
Both routes use `perseus-mcp` through an in-process MCP client; a separate Perseus server is not needed.
For setup details, see the [Perseus MCP documentation](https://tonyjurg.github.io/Perseus-mcp/).
The recorded Greek runs use version 1.0.2 ([DOI](https://doi.org/10.5281/zenodo.20931139)).
A descriptive document on Perseus MCP is available at [doi:10.5281/zenodo.23664266](https://doi.org/10.5281/zenodo.23664266).

**Reception history**

```powershell
conda create -n hakhel-reception python=3.13 -y
conda activate hakhel-reception
python -m pip install -r ".\reception_history\requirements.txt"
python -m pip install ipykernel
python -m ipykernel install --user --name hakhel-reception --display-name "Hakhel - Reception history"
python -m pip check
```

The Python versions above are setup choices for new environments, not a claim that all recorded runs used them.
Select the named kernel in Jupyter for each notebook rather than relying on an existing `base` or `python3` selection.
To confirm the kernel's interpreter, run `import sys; print(sys.executable)` in a temporary cell.

# 3 - Obtain BHSA 2021<a class="anchor" id="bullet3"></a>
##### [Back to ToC](#TOC)

The corpus is intentionally excluded from Git.
The recorded Context-Fabric provenance identifies commit `4db00e2157915495e1a4d3d57e41223df24775da` in ETCBC/bhsa and the `tf/2021` directory.
For a fresh corpus directory, run these commands from the repository root:

```powershell
New-Item -ItemType Directory -Force -Path ".\context_fabric\data" | Out-Null
git init ".\context_fabric\data\bhsa"
Push-Location ".\context_fabric\data\bhsa"
git remote add origin https://github.com/ETCBC/bhsa.git
git sparse-checkout init --cone
git sparse-checkout set tf/2021
git fetch --depth 1 origin 4db00e2157915495e1a4d3d57e41223df24775da
git checkout --detach FETCH_HEAD
git rev-parse HEAD
Pop-Location
```

Check that the printed commit matches the one above and that `context_fabric/data/bhsa/tf/2021/otype.tf` and `oslots.tf` exist.
If the corpus already exists, inspect its commit and local changes before changing it; the commands above assume a new checkout.
Context-Fabric builds its `.cfm` cache on first use.
The cache can be large, and compilation may take several minutes and several gigabytes of memory; the cache does not need to be copied from the author.

# 4 - Run the notebooks in order<a class="anchor" id="bullet4"></a>
##### [Back to ToC](#TOC)

For each notebook, restart its kernel and run the cells from the top.
Use the working directories below because some paths still depend on the kernel's current directory.

| Order | Notebook | Kernel | Kernel working directory |
|---|---|---|---|
| 1 | [Context-Fabric](context_fabric/hakhel_bhsa.ipynb) | Hakhel - Context-Fabric | `context_fabric` |
| 2 | [SHEBANQ controls](SHEBANQ-BHSA/shebanq_controls.ipynb) | Hakhel - SHEBANQ | `SHEBANQ-BHSA` |
| 3 | [Main LXX passages](lxx/hakhel_lxx.ipynb) | Hakhel - Greek texts | `lxx` |
| 4 | [42-row LXX alignment](lxx/taf_lxx_alignment.ipynb) | Hakhel - Greek texts | `lxx` |
| 5 | [Philo](philo/hakhel_philo.ipynb) | Hakhel - Greek texts | `philo` |
| 6 | [Reception history](reception_history/hakhel_reception.ipynb) | Hakhel - Reception history | `reception_history` |

Only the Hebrew controls and alignment depend on the Context-Fabric outputs.
Philo and reception history can be run independently.
The alignment requires both `context_fabric/results/taf_occurrences.csv` and `context_fabric/results/audit.json`.
SHEBANQ requires the occurrence CSV.
These files are included as recorded results, so the later notebooks can also use them without rerunning the Hebrew retrieval.

For Context-Fabric, activate its environment and start the local server from the repository root:

```powershell
conda activate hakhel-context
$env:CONTEXT_FABRIC_PYTHON = (Get-Command python).Source
& ".\context_fabric\start_local_server.ps1" -Python $env:CONTEXT_FABRIC_PYTHON
```

Leave that terminal running.
In a second Anaconda PowerShell terminal, activate the same environment, set the variable again, and open the notebook:

```powershell
conda activate hakhel-context
$env:CONTEXT_FABRIC_PYTHON = (Get-Command python).Source
Set-Location ".\context_fabric"
jupyter lab "hakhel_bhsa.ipynb"
```

The second terminal's `Set-Location` command assumes it starts in the repository root.
The notebook can also start the server when the port is free, but starting it separately makes the startup messages easier to inspect.

For the other notebooks, activate the matching environment, change to its directory, and open the notebook with `jupyter lab`.
For example, from the repository root:

```powershell
conda activate hakhel-reception
Set-Location ".\reception_history"
jupyter lab "hakhel_reception.ipynb"
```

The Context-Fabric command-line wrapper uses a kernel named `python3` explicitly.
The named kernels registered above do not change that setting; use the interactive route in this guide unless you separately configure the wrapper's kernel.

# 5 - Check and record the results<a class="anchor" id="bullet5"></a>
##### [Back to ToC](#TOC)

A notebook reaching its final cell does not establish that every request succeeded.
Read the audits and review tables, as well as any failed assertions.

* **Context-Fabric:** expect 42 occurrences with unique references, complete contextual mapping, and the selected Hebrew phrases found in their verses.
* **SHEBANQ:** expect the all-טף control to match all 42 Context-Fabric word slots and mapped references; the negative audience control should be empty.
* **LXX alignment:** retain all 42 input rows and inspect retrieval failures, reference cautions, and lexical candidates in the review queue.
* **Philo:** inspect search-page errors and passage-retrieval failures; the search collects at most two pages per term, so its results are a bounded survey.
* **Reception history:** inspect missing curated references, failed text requests, and queries that reached the result limit in the run's audit.

The current reception-history run is identified by [current_run.json](reception_history/results/current_run.json).
It records 345 text requests, 344 successful texts, and one failure; all curated references are present, but the complete retrieval still has one gap.
The notebook creates a new dated run directory but does not automatically update the current-run pointer.
Review the new results before changing that pointer.
Other notebooks generally overwrite their named result files.

Record the repository commit, corpus commit, Python version, package versions, execution date, and audit results with your new run.
The LXX and Philo notebooks use the shared `notebook_provenance.py` helper at the repository root; keep it with the notebooks.
Their provenance exports and `run_timing.json` record UTC run start/completion, per-request retrieval start/end and dates, software versions, source editions, and service endpoints.
Run timestamps are recorded during execution, not copied from notebook author/date labels.
An interrupted run retains its request log with no completion time; an exported run may still contain retrieval failures, so inspect its corpus audit as well.
Context-Fabric and Sefaria also record their execution times.
For each activated environment, these commands can help capture the software state:

```powershell
python --version
python -m pip check
python -m pip freeze
```

Save the output outside the recorded result files, or under a clearly identified new run.
A package list records an environment; it does not by itself guarantee that identical binaries will be available on every operating system.

# 6 - Common problems and current limits<a class="anchor" id="bullet6"></a>
##### [Back to ToC](#TOC)

| Symptom | What to check |
|---|---|
| Python points to an old folder | Recreate the environment; do not reuse a moved virtual environment. Set `CONTEXT_FABRIC_PYTHON` and pass `-Python` to the launcher. |
| Import error involving `FastMCP` | Check the MCP pin in the relevant requirements file and confirm the notebook kernel belongs to that environment. |
| Port 8765 is already occupied | Check which service is listening before starting another server. The notebook expects Context-Fabric there. |
| File not found despite a successful clone | Check the kernel working directory, authored inputs, and required Context-Fabric exports. |
| A hosted service returns fewer or different results | Inspect errors, limits, source versions, and raw responses before interpreting the difference. |

Some dependency requirements are minimum versions rather than a complete lockfile.
The provenance records the package versions used during execution.
All six notebooks have successful executions dated 26 October 2026, using Python 3.14.2.
The five MCP-based notebooks use MCP 1.30.0; the SHEBANQ notebook retrieves its public controls over HTTP and confirms that all 42 word slots and references match the BHSA occurrence set.

Online availability, search limits, source revisions, and unresolved rights information remain part of the reproduction record.
The raw responses and audits help explain differences, while the curated files preserve the research choices.
For methods and interpretation, read the directory READMEs and the explanatory cells in each notebook.
