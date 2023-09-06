# acme lab tools

## Installation

```sh
pip install --upgrade git+https://github.com/vinhowe/acme-lab-tools
```

## Usage

Convert a python script to a notebook:

```sh
python3 -macme_tools.pyify --force standard_library.py
```

Convert a notebook to a python script:

```sh
python3 -macme_tools.pyify --force standard_library.ipynb
```