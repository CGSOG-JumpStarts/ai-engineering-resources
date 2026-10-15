"""Offline structural/security audit for enterprise engineering package."""
from pathlib import Path
from urllib.parse import unquote
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
 'README.md','START-HERE.md','SOURCES.md',
 '01-spec-driven-development/framework-comparison.md',
 '03-azure-ai-foundry/reference-architecture.md',
 '04-engineering-guardrails/secure-mcp-practices.md',
 '05-evaluation/scorecard-template.md',
 '06-reference-lab/specs/dealer-support-advisor.md',
 '06-reference-lab/scripts/evaluate.py',
]
SKILLS = ['foundry-docs-advisor','spec-reviewer','secure-mcp-review','agent-evaluation-designer']


def check_bundle() -> list[str]:
    problems = []
    for item in REQUIRED:
        if not (ROOT/item).is_file(): problems.append('Missing expected file: '+item)
    for name in SKILLS:
        p=ROOT/'02-agent-skills'/name/'SKILL.md'
        if not p.is_file():
            problems.append('Missing skill: '+name)
            continue
        t=p.read_text()
        match=re.match(r'\A---\n(.*?)\n---\n',t,re.DOTALL)
        if not match:
            problems.append('Invalid skill frontmatter: '+name)
            continue
        fm=match.group(1)
        n=re.search(r'^name:\s*(.+)$',fm,re.MULTILINE)
        d=re.search(r'^description:\s*(.+)$',fm,re.MULTILINE)
        if not n or n.group(1).strip()!=name: problems.append('Skill name mismatch: '+name)
        if not d or not d.group(1).strip() or len(d.group(1))>1024: problems.append('Skill description invalid: '+name)
    for p in ROOT.rglob('*'):
        if not p.is_file() or '.cache' in p.parts or '.reports' in p.parts or '__pycache__' in p.parts:
            continue
        if p.suffix not in {'.md','.py','.js','.json','.html','.css','.csv','.yml','.yaml','.txt'}: continue
        content=p.read_text(encoding='utf-8',errors='replace')
        if '\x08' in content or '\x00' in content:
            problems.append('Binary control in text file: '+str(p.relative_to(ROOT)))
        # These two in-development sibling projects are intentionally excluded from this handoff.
        banned = ''.join(['auto','pilot'])
        banned2 = ''.join(['aiq','ecp'])
        if re.search(re.escape(banned)+'|'+re.escape(banned2),content,re.IGNORECASE) and p.name!='validate_bundle.py':
            problems.append('Excluded sibling-project reference: '+str(p.relative_to(ROOT)))
        if p.suffix=='.md':
            for link in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)',content):
                dest=link.strip().split('#',1)[0]
                if not dest or dest.startswith(('http://','https://','mailto:','<','/')):
                    continue
                # Strip optional markdown link title (not used in this package).
                dest=unquote(dest).split(' "',1)[0]
                if not (p.parent/dest).exists():
                    problems.append(f'Broken local Markdown link in {p.relative_to(ROOT)}: {dest}')
    for rel in ['06-reference-lab/specs/traceability.json','06-reference-lab/evaluation/cases.json','02-agent-skills/foundry-docs-advisor/references/upstream.json']:
        try: json.loads((ROOT/rel).read_text())
        except Exception as e: problems.append('Invalid JSON '+rel+': '+str(e))
    return problems

if __name__=='__main__':
    errors=check_bundle()
    if errors:
        print('Bundle audit FAILED:')
        for e in errors:print(' -',e)
        sys.exit(1)
    print('Bundle audit PASSED: sources, local Markdown links, metadata, expected files and exclusions')
