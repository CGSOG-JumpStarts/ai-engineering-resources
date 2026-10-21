"""Run companion examples; opt into temporary loopback HTTP with --http."""
import argparse
from pathlib import Path
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--http", action="store_true", help="Include the localhost HTTP example")
    args = parser.parse_args()
    examples = ["first_answer.py", "trace_contract.py", "mixed_intent_lab.py", "evaluate_traces.py"]
    if args.http:
        examples.append("http_roundtrip.py")
    folder = Path(__file__).resolve().parent
    for name in examples:
        print(f"\n--- {name} ---", flush=True)
        subprocess.run([sys.executable, str(folder / name)], check=True, timeout=30)
    print(f"\n{len(examples)} companion programs completed.")


if __name__ == "__main__":
    main()
