"""Check staged filenames and notebook outputs; stdlib only."""
import json
from pathlib import PurePosixPath
import subprocess
allowed = {"README.md", ".gitignore", "requirements.txt", ".vscode/settings.json", "架构与优化说明.md", "项目使用说明.md", "CNN混凝土裂缝识别复现.ipynb"}
result = subprocess.run(["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z"],
                        check=True, stdout=subprocess.PIPE)
for filename in result.stdout.decode("utf-8").split("\0"):
    if not filename:
        continue
    path = PurePosixPath(filename)
    ok = filename in allowed or (path.parts[0] == "scripts" and path.suffix == ".py")
    ok = ok or (path.parts[0] == "notebooks" and path.suffix == ".ipynb")
    ok = ok or filename in {".githooks/pre-commit", ".githooks/pre-push"}
    if not ok:
        raise SystemExit("Rejected non-source file: " + filename)
    if path.suffix == ".ipynb":
        raw = subprocess.run(["git", "show", ":"+filename], check=True, stdout=subprocess.PIPE).stdout
        nb = json.loads(raw.decode("utf-8"))
        if any(c.get("outputs") or c.get("execution_count") is not None for c in nb["cells"] if c["cell_type"] == "code"):
            raise SystemExit("Clear outputs then stage again: " + filename)
print("Staged source-only checks passed.")
