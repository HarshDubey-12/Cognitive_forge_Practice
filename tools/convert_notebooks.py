"""Convert all .ipynb notebooks (excluding checkpoints) to Python scripts in src/.

Usage:
    python tools/convert_notebooks.py

It will write one .py per notebook into src/ using the notebook filename (sanitized).
"""
import io
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(__file__))
SRC_DIR = os.path.join(ROOT, "src")

os.makedirs(SRC_DIR, exist_ok=True)


def sanitize(name: str) -> str:
    name = re.sub(r"\.ipynb$", "", name, flags=re.IGNORECASE)
    name = name.strip()
    name = re.sub(r"[^0-9A-Za-z_]+", "_", name)
    name = re.sub(r"_+", "_", name)
    return name.lower()


def notebook_to_script(notebook_path: str, out_path: str):
    with io.open(notebook_path, "r", encoding="utf-8") as f:
        nb = json.load(f)
    cells = nb.get("cells", [])
    code_lines = [
        "# Auto-generated from: {}\n".format(os.path.basename(notebook_path)),
        "# Run as a script or import functions from this module.\n\n",
    ]
    for cell in cells:
        if cell.get("cell_type") == "code":
            source = cell.get("source", [])
            # source can be list of lines or a single string
            if isinstance(source, list):
                code_lines.extend([line if line.endswith("\n") else line + "\n" for line in source])
            else:
                code_lines.append(source + "\n")
            code_lines.append("\n")
    with io.open(out_path, "w", encoding="utf-8") as f:
        f.writelines(code_lines)


def main():
    converted = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        # skip .ipynb_checkpoints and the src/tools folders
        if ".ipynb_checkpoints" in dirpath:
            continue
        # don't scan src/ to avoid converting generated scripts
        if os.path.abspath(dirpath).startswith(os.path.abspath(SRC_DIR)):
            continue
        for fn in filenames:
            if fn.lower().endswith(".ipynb"):
                # skip checkpoint files
                if "checkpoint" in fn.lower():
                    continue
                nb_path = os.path.join(dirpath, fn)
                base = sanitize(fn)
                out_file = os.path.join(SRC_DIR, f"{base}.py")
                try:
                    notebook_to_script(nb_path, out_file)
                    converted.append((nb_path, out_file))
                except Exception as e:
                    print(f"Failed to convert {nb_path}: {e}")
    print(f"Converted {len(converted)} notebooks to {SRC_DIR}")
    for src, out in converted:
        print(f" - {os.path.relpath(src, ROOT)} -> {os.path.relpath(out, ROOT)}")


if __name__ == "__main__":
    main()
