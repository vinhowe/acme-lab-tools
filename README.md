# acme lab tools

Tool to convert between Python scripts and Jupyter notebooks with an ease-of-use feature for ACME lab assignments.

## Installation

```sh
pip install --upgrade git+https://github.com/vinhowe/acme-lab-tools
```

## Usage

All code in the Python script will be converted to cells in the notebook. Each cell will start with `# acme-include`. Any cells not marked with `# acme-include` will be ignored when converting back to a Python script. This makes it easy to write test code inline with your assignment code without having to remove it from the submitted Python script.

Convert a python script to a notebook:

```sh
python3 -macme_tools.pyify --force standard_library.py
```

Convert a notebook to a python script:

```sh
python3 -macme_tools.pyify --force standard_library.ipynb
```