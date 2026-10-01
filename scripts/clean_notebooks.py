"""Remove notebook execution outputs before committing source."""
from pathlib import Path
import json
root = Path(__file__).resolve().parents[1]
for path in sorted(root.glob("*.ipynb")):
    nb = json.loads(path.read_text(encoding="utf-8"))
    for cell in nb["cells"]:
        if cell["cell_type"] == "code":
            cell["outputs"] = []
            cell["execution_count"] = None
    path.write_text(json.dumps(nb, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Cleaned:", path.name)
