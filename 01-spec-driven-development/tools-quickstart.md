# Trying public spec-driven development tools

Use a scratch repository with fictional data first. Commands below reflect vendor-maintained documentation rechecked on **21 October 2026**. Check current prerequisites, release tags, supply-chain policy and tool integration names before installation.

## GitHub Spec Kit

Official source: [github/spec-kit](https://github.com/github/spec-kit). Official CLI reference: [Specify init](https://github.com/github/spec-kit/blob/main/docs/reference/core.md).

The vendor documents Python 3.11+, `uv` and the Specify CLI. This prerequisite differs from the offline lab's Python 3.10+ requirement. In an approved terminal:

```bash
uv tool install specify-cli
specify init sample-feature --integration copilot
```

The commands above are terminal setup. Spec Kit's `/speckit-*` skills are invoked in the coding assistant's chat; do not paste them into the shell. Read the current [installation](https://github.github.io/spec-kit/installation.html) and [quickstart](https://github.github.io/spec-kit/quickstart.html) guides for your integration. Record the installed CLI release/revision, integration and extensions alongside the pilot. The observed v1.2.2 release is not a tested dependency pin in this package.

Before implementation, inspect generated plans and use clarify/checklist/analyze for unresolved questions or consistency review. The current quickstart records active feature state in `.specify/feature.json`; a Git branch switch alone does not establish which feature the assistant will use. Check the selected feature when resuming work.

## BMad Method stable release

Official [installation guide](https://docs.bmad-method.org/start/install-bmad/) explicitly differentiates the stable **v6.12** path from **v7 preview alpha** (as checked 2026-10-21). The stable path lists Node.js 20.12+, Python 3.10+ and uv, and the command:

```bash
npx bmad-method install
```

The later skills/marketplace instructions on that page describe the v7 preview path. Do not mix them with a v6.12 setup by assumption. Review the exact version resolved by npm and pin it for team trials. Do not use the moving preview as the default reference for a reliability-focused pilot.

## Microsoft HVE Core

Official [repository](https://github.com/microsoft/hve-core) and [getting-started documentation](https://github.com/microsoft/hve-core/blob/main/docs/getting-started/README.md). Read the **RPI phase guidance** before importing tools. HVE itself notes that its workflow can change substantially without stable backwards compatibility. Prefer a pinned revision, small trial and explicit review of commands/scripts rather than a blind install.

## Jump Start AutoNav (optional)

An [author-provided framework reference](https://github.com/otey247/JumpStart-AutoNav) is optional. This update did not verify its access, released version or distribution rights. Request a reviewed demo or shareable distribution from the owner before evaluating it. It is not a dependency of this package.

## Important

Avoid installing two independent frameworks into the same repository for the same task without an integration design. Use one workflow, a small fixed use case and common measures for review effort, acceptance coverage and final quality.
