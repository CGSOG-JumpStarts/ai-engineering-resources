"""Validate spec -> acceptance criterion -> existing Python test method links."""
import ast
import json
from pathlib import Path
import re
import sys
ROOT = Path(__file__).resolve().parents[1]


def validate() -> list[str]:
    errors = []
    mapping = json.loads((ROOT/'specs/traceability.json').read_text())
    spec = (ROOT/mapping['spec']).read_text()
    declared_ac = set(re.findall(r'^- `(AC-\d{3})`:', spec, flags=re.MULTILINE))
    requirements = set(re.findall(r'^- `((?:FR|NFR)-\d{3})`:', spec, flags=re.MULTILINE))
    covered = set()
    mapped_requirements = set()
    for item in mapping['coverage']:
        ac = item['ac']
        if ac in covered:
            errors.append(f'duplicate mapping: {ac}')
        covered.add(ac)
        if ac not in declared_ac:
            errors.append(f'mapping references nonexistent {ac}')
        for req in item['requirements']:
            mapped_requirements.add(req)
            if req not in requirements:
                errors.append(f'{ac} references nonexistent requirement {req}')
        target = ROOT/item['test_file']
        if not target.is_file():
            errors.append(f'{ac}: missing file {item["test_file"]}')
        else:
            tree = ast.parse(target.read_text())
            methods = {n.name for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
            if item['test_method'] not in methods:
                errors.append(f'{ac}: missing test method {item["test_method"]}')
    for ac in sorted(declared_ac-covered):
        errors.append(f'uncovered criterion: {ac}')
    for req in sorted({x for x in requirements if x.startswith('FR-')} - mapped_requirements):
        errors.append(f'functional requirement missing acceptance coverage: {req}')
    if not declared_ac:
        errors.append('no acceptance criteria parsed from spec')
    if not requirements:
        errors.append('no requirements parsed from spec')
    return errors

if __name__ == '__main__':
    problems = validate()
    if problems:
        print('Contract check FAILED:')
        for x in problems: print(' -',x)
        sys.exit(1)
    print('Contract check PASSED: all declared acceptance criteria map to existing tests and requirements')
