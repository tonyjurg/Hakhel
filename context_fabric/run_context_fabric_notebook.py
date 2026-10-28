"""This Python code will run the Context Fabric notebook and save its completed outputs.

This is an execution wrapper, not a notebook builder. It does not compose
Markdown, insert code cells, or supply research data. The authored notebook is
loaded as it stands and executed from beginning to end in the ``context_fabric``
directory. Only a successful run is written back to the notebook; an error in
any cell stops execution before the file is replaced.

Keeping this small wrapper in the repository provides a repeatable command-line
route for the same notebook that can also be opened and run interactively.
"""

from pathlib import Path

import nbformat
from nbclient import NotebookClient


HERE = Path(__file__).resolve().parent
NOTEBOOK = HERE / "hakhel_bhsa.ipynb"


def main() -> None:
    """Execute the notebook in its own directory and save the resulting run."""
    with NOTEBOOK.open("r", encoding="utf-8") as handle:
        notebook = nbformat.read(handle, as_version=4)

    client = NotebookClient(
        notebook,
        timeout=1200,
        kernel_name="python3",
        resources={"metadata": {"path": str(HERE)}},
        allow_errors=False,
    )
    client.execute()

    with NOTEBOOK.open("w", encoding="utf-8") as handle:
        nbformat.write(notebook, handle)

    print(f"Executed and saved {NOTEBOOK}")


if __name__ == "__main__":
    main()
