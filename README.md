# agentic-system

Python project scaffold with a src layout, CLI entry point, and tests.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python -m ipykernel install --user --name agentic-system --display-name "agentic-system"
```

## Environment variables

Copy `.env.example` to `.env` and add secrets there. `.env` is gitignored.

In a notebook:

```python
from dotenv import load_dotenv

load_dotenv()
```

## Notebooks

Open files in `notebooks/` and choose the **agentic-system** kernel.

```powershell
jupyter notebook notebooks
```

## Run

```powershell
python -m agentic_system
agentic-system
```

## Test

```powershell
pytest
```
