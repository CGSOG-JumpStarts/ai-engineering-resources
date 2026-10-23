# Spec-driven engineering workflows

## What do the public tools document as of October 21, 2026?

### Takeaway

The comparison remains useful, but needs a dated release recheck and lighter entry paths. Record release tags, moving documentation and installed integration separately.

### Cited Findings

- Checked 2026-10-21: Spec Kit releases list **v1.2.2**, dated October 19, as Latest, with a version-pinned source-install example. This is a release observation, not local qualification. — [Releases](https://github.com/github/spec-kit/releases)
- Spec Kit provides separate feature SDD, bug-fixing and idea-assessment processes. SDD is core; bug/assessment are opt-in extensions. Its feature flow is constitution once, then specify/plan/tasks/implement/converge. Community catalogs are not audits. — [README](https://github.com/github/spec-kit)
- Specify requires Python 3.11+. Maintained source and PyPI channels are documented; source installs pinned to a release tag are recommended. `specify version` checks version/runtime, not package provenance. Windows PowerShell is supported. — [Installation](https://github.github.io/spec-kit/installation.html)
- The quickstart uses `/speckit-*` skills in Copilot chat, separate from terminal setup. Clarify resolves uncertainty; analyze reports cross-artifact conflicts; converge checks implementation and can append tasks. Checked custom requirement checklists represent requirements review, not implementation completion. Active feature state is recorded in `.specify/feature.json`; switching Git branches alone does not select a feature. — [Quickstart](https://github.github.io/spec-kit/quickstart.html)
- Checked 2026-10-21: BMad installation still labels **v7 preview alpha** and **v6.12 stable**. Its retained October 16 ETA has elapsed; that is not release evidence. The stable command is `npx bmad-method install`; later skills/marketplace instructions apply to v7. Skills execute with the coding host's permissions. — [Install](https://docs.bmad-method.org/start/install-bmad/)
- BMad releases list **v6.12.4**, dated October 14, as Latest. v6.12.0 notes describe smaller specs for simple changes and review findings with recorded dispositions. — [Releases](https://github.com/bmad-code-org/BMAD-METHOD/releases)
- HVE Core warns against treating it as a stable platform or production dependency. Its README documents VS Code/Copilot CLI entry points and license exceptions for some derived skill content. — [README](https://raw.githubusercontent.com/microsoft/hve-core/main/README.md)

### Inferences

1. Update `framework-comparison.md` and `tools-quickstart.md` to October 21. Keep dated release observations separate from tested commands. Distinguish Spec Kit's Python 3.11+ from the lab's 3.10+.
2. Explain terminal setup versus assistant chat skills. Record the CLI tag, integration and selected extensions in team trials. Do not promote BMad v7 from its elapsed ETA or imply catalogue listings establish safety.

### Gaps

No installers, registry artifacts, assistant integrations or private repositories were tested. AutoNav access/version/distribution rights remain unverified. BMad's actual v7 completion schedule is uncertain.

## How much specification and research should a change receive?

### Takeaway

Current workflows support bounded changes and selective research. Choose artifacts for unresolved decisions and risks, rather than requiring a complete lifecycle for every edit.

### Cited Findings

- HVE RPI documentation dated October 16 says supplied evidence should be reused when adequate and research should address a demonstrated gap. It permits direct phase skills and smaller edits. Follow-up routes defects to implementation, decision gaps to planning and evidence gaps to research. Review execution status is distinct from acceptance outcome. — [RPI](https://raw.githubusercontent.com/microsoft/hve-core/main/docs/rpi/README.md)
- BMad's planning guide defines intent through intended outcomes, preserved constraints and excluded work. Obvious low-risk edits need no BMad workflow. More planning is justified by uncertainty, architectural reach, cross-system effects and coordination. Research/design tools are selected for a gap rather than compulsory stages. — [Planning path](https://docs.bmad-method.org/plan/choose-a-planning-path/)
- BMad's brownfield guidance emphasizes current source and tight project context; existing maintained instructions can replace context generation. Requirements/architecture should cite current structures, and changed patterns need a recorded reason. Confirm current commands against a v6.12 installation. — [Existing codebases](https://docs.bmad-method.org/existing-codebases/start-in-an-existing-codebase/)

### Inferences

3. Add a compact sizing table: isolated edit -> acceptance check/review; new feature -> spec/plan/tasks/negative tests; uncertain integration -> evidence for decisions plus contracts/failure tests. Label this editorial guidance, not company policy.
4. Expand brownfield guidance with a preservation list: public schema, authorization, failure codes and migration constraints; link source locations and regression checks. Give open questions an owner and blocking status. Do not require a full-system specification before a bounded change.

### Gaps

No controlled evidence was found here for universal productivity percentages, optimum document counts or token savings. Real organizational review requirements remain outside this synthetic package.

## How should specifications remain trustworthy after delivery?

### Takeaway

Choose a maintenance convention and review contract, code and evidence together. A surprising implementation cannot decide its own intended requirement.

### Cited Findings

- Spec Kit's brownfield guide starts with a reviewable baseline and bounded next change. Initialization may replace conflicting managed files. It asks teams to choose how artifacts age: historical records, maintained contracts, or accepted discoveries reconciled across artifacts. — [Existing projects](https://github.github.io/spec-kit/guides/existing-projects.html)
- Spec Kit separates managed framework upgrades from evolving feature artifacts; no persistence model is required/default. Converge only appends tasks, and analyze reports inconsistencies without reconciling them. Teams decide which discoveries to accept and update artifacts, preserving relevant rationale. — [Evolving specs](https://github.github.io/spec-kit/guides/evolving-specs.html)

### Inferences

5. Add a maintenance section: name the authoritative spec and owner, distinguish historical snapshots from current contracts, link superseded versions, and reconcile plan/tasks/tests after reviewed changes of intent.
6. Add a synthetic drift example: if code answers coverage guarantees while AC-004 requires escalation, report a defect. If an owner later accepts different behavior, revise the spec and negative cases before code. Keep framework/template upgrades reviewable separately from feature delivery.

### Gaps

No runtime behavior or stable acceptance IDs were changed. Actual enterprise retention/change policies were not assessed. Sources were retrieved October 21; moving pages are not immutable snapshots.
