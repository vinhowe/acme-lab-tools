import json
import subprocess
import sys
import tempfile
from pathlib import Path


def pyify(file: Path, force=False):
    # Create a temporary file
    py_path = file.with_suffix(".py")
    if py_path.exists() and not force:
        print(
            f"{py_path} already exists, skipping... (use --force to overwrite)",
            file=sys.stderr,
        )
        return

    with tempfile.NamedTemporaryFile(suffix=".ipynb", delete=False, mode="w+") as tmp:
        with open(file, "r") as f:
            data = json.load(f)
            data["cells"] = [
                # Cell without first line
                {
                    **cell,
                    "source": cell["source"][1:],
                }
                for cell in data["cells"]
                if cell["source"] and cell["source"][0].startswith("# acme-include")
            ]
            # Write the json to the temporary file
            json.dump(data, tmp)
        # Use jupytext to convert the temporary file to a python file (same
        # name as the input file with a .py extension, using pathlib to replace)
    subprocess.run(
        [
            "python3",
            "-m",
            "jupytext",
            "--to",
            "py",
            tmp.name,
            "--output",
            str(Path(file).with_suffix(".py")),
        ]
    )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert ipynb files to py files")
    parser.add_argument("files", nargs="+", type=Path, help="ipynb files to convert")
    parser.add_argument("--force", action="store_true", help="overwrite existing files")

    args = parser.parse_args()
    for file in args.files:
        pyify(file, args.force)
