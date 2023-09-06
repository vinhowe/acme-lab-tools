import json
import subprocess
import sys
from pathlib import Path


def nbify(file: Path, force=False) -> None:
    notebook_path = file.with_suffix(".ipynb")
    if notebook_path.exists() and not force:
        print(
            f"{notebook_path} already exists, skipping... (use --force to overwrite)",
            file=sys.stderr,
        )
        return

    subprocess.run(
        [
            "python3",
            "-m",
            "jupytext",
            "--to",
            "notebook",
            file,
            "--output",
            notebook_path,
        ]
    )
    # Read the ipynb file as json, add "#acme-include\n" to all cells
    with open(notebook_path, "r") as f:
        data = json.load(f)
        for cell in data["cells"]:
            cell["source"].insert(0, "# acme-include\n")
        with open(notebook_path, "w") as f:
            json.dump(data, f)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert ipynb files to py files")
    parser.add_argument("files", nargs="+", type=Path, help="ipynb files to convert")
    parser.add_argument("--force", action="store_true", help="overwrite existing files")

    args = parser.parse_args()
    for file in args.files:
        nbify(file, args.force)
