"""Follow AC-004 to its real test source. This does not execute the test."""
import ast
import json
from pathlib import Path

LAB = Path(__file__).resolve().parents[2] / "06-reference-lab"


def main():
    mapping = json.loads((LAB / "specs" / "traceability.json").read_text(encoding="utf-8"))
    entry = next(item for item in mapping["coverage"] if item["ac"] == "AC-004")
    spec = (LAB / mapping["spec"]).read_text(encoding="utf-8")
    criterion = next(line for line in spec.splitlines() if line.startswith("- `AC-004`:"))
    source = (LAB / entry["test_file"]).read_text(encoding="utf-8")
    method = next(node for node in ast.walk(ast.parse(source))
                  if isinstance(node, ast.FunctionDef) and node.name == entry["test_method"])
    print(criterion)
    print("Requirements: " + ", ".join(entry["requirements"]))
    print(f"Test: {entry['test_file']}::{entry['test_method']}")
    print("\nExisting test source:")
    print(ast.get_source_segment(source, method))
    print("\nSource located; test execution is a separate step.")


if __name__ == "__main__":
    main()
