# Environment setup

Create and activate a virtual environment, then install required packages.

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

Unix / macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

Notes:
- `requirements.txt` contains runtime dependencies for the example scripts.
- `requirements-dev.txt` contains testing and formatting tools.
