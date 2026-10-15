"""Deterministic golden-case evaluator; not a Foundry model benchmark."""
import json
import math
from pathlib import Path
import sys
from time import perf_counter
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from dealer_advisor import AdviceService, DemoPrincipal, InputError

ROOT=Path(__file__).resolve().parents[1]

def pct(values, pct):
    if not values: return None
    ordered=sorted(values)
    return round(ordered[max(0, math.ceil(pct*len(ordered))-1)], 4)


def run(cases=None):
    service=AdviceService()
    cases=cases if cases is not None else json.loads((ROOT/'evaluation/cases.json').read_text())
    rows=[]
    for case in cases:
        principal=DemoPrincipal('SYN-DEALER-100', frozenset(case.get('principal_scopes', ['advice:read'])))
        start=perf_counter()
        try:
            result=service.answer(case['question'],principal).as_dict()
            observed_status=result['status']
            observed_source=(result['source_ids'] or [None])[0]
            observed_tool=(result['tool_calls'] or [None])[0]
            error=None
        except InputError as ex:
            observed_status='error'
            observed_source=None
            observed_tool=None
            error=ex.code
        elapsed_ms=(perf_counter()-start)*1000
        passed=(observed_status==case['expected_status']
                and observed_source==case.get('expected_source')
                and observed_tool==case.get('expected_tool')
                and error==case.get('expected_error'))
        rows.append({'case_id':case['id'],'passed':passed, 'expected_status':case['expected_status'],
                     'observed_status':observed_status,'observed_source':observed_source,
                     'observed_tool':observed_tool,'error':error,'elapsed_ms':round(elapsed_ms,4)})
    good=sum(x['passed'] for x in rows)
    return {'lab':'synthetic-deterministic','model_calls':0,'model_tokens':None,'model_cost_usd':None,
            'cases':len(rows),'passed':good,'failed':len(rows)-good,
            'pass_rate':round(good/len(rows),4) if rows else None,
            'latency_ms':{'p50':pct([x['elapsed_ms'] for x in rows],.5),'p95':pct([x['elapsed_ms'] for x in rows],.95)},
            'results':rows,
            'caveat':'Timing only measures in-process deterministic decisions; model and production effectiveness are not evaluated.'}


def main():
    report=run()
    out=ROOT/'.reports'
    out.mkdir(exist_ok=True)
    (out/'evaluation-report.json').write_text(json.dumps(report,indent=2)+'\n')
    md=['# Local golden-case evaluation','',f"Synthetic tests: {report['passed']} / {report['cases']} passed",
        f"p50 / p95 decision latency: {report['latency_ms']['p50']} / {report['latency_ms']['p95']} ms",
        '', '> No LLM calls. Provider token/cost metrics are not applicable.', '', '| Case | Result | Expected | Actual |', '|---|---|---|---|']
    md += [f"| {r['case_id']} | {'PASS' if r['passed'] else 'FAIL'} | {r['expected_status']} | {r['observed_status']} |" for r in report['results']]
    md+=['','',report['caveat']]
    (out/'evaluation-report.md').write_text('\n'.join(md)+'\n')
    print(f"Golden evaluation: {report['passed']}/{report['cases']} passed. Report: {out/'evaluation-report.json'}")
    if report['failed']: sys.exit(1)

if __name__=='__main__': main()
