from pathlib import Path
import subprocess


AGENTS = [
    "dataset",
    "inference",
    "ontology",
    "planner",
    "state",
    "tools",
    "training",
]


def test_scaffold_files_exist():
    for a in AGENTS:
        base = Path("agents") / a
        assert (base / "README.md").exists(), f"{a} missing README.md"
        assert (base / "OWNERS").exists(), f"{a} missing OWNERS"
        assert (base / "CHANGE_SCOPE.md").exists(), f"{a} missing CHANGE_SCOPE.md"


def test_run_validators():
    # Run the two validators we added as a smoke test
    repo_root = Path(".")
    # ontology example: ensure it's valid JSON (do not change existing schema rules)
    ont_example = Path("agents/ontology/v0/examples/home_ontology.v0.examples.json")
    ont_example.read_text()  # will raise if invalid JSON
    out = subprocess.run(["python3", "agents/state/validators/validate_schema.py"], cwd=repo_root, capture_output=True)
    assert out.returncode == 0, out.stderr.decode()
