# Decision Gates

Use gates to prevent review signals from becoming unverified changes.

## Evidence Gate

Every accepted finding needs:

- source path or record identifier
- exact observed behavior or value
- expected behavior or rule
- command/test/log/report supporting the claim
- confidence and scope

If evidence is absent, mark as manual review.

## Change Gate

Before changing code, data, rules, schema, or prompts, require:

- stated root cause or hypothesis
- affected surface area
- rollback or recovery note for risky changes
- validation command or deterministic check
- owner for follow-up

## Model Output Gate

Model outputs are interpretations.

Accept only after:

- mapping model row IDs or claims back to source evidence
- checking whether the prompt exposed enough context
- checking for hallucinated facts
- comparing against deterministic checks where available
- recording why the output was accepted or rejected

## Disagreement Gate

When reviewers disagree:

1. Write the conflict in one sentence.
2. Identify the source fact that could settle it.
3. If a source fact exists, Codex verifies it.
4. If no source fact exists, route to manual review or design a probe.
5. Do not use majority vote as the deciding rule.

## Release Gate

Before release or production-facing change:

- tests/checks pass or failures are explained
- risk class is explicit
- migration/rollback is defined if needed
- observability or audit output exists for risky paths
- user-facing impact is documented

## ADR/RFC Gate

Create an ADR/RFC when a decision changes:

- architecture
- public API or schema
- security/privacy posture
- data lineage or audit policy
- model-review policy
- operational ownership

Minimum ADR:

```markdown
# ADR: <title>

## Context
## Decision
## Evidence
## Options Considered
## Consequences
## Rollback / Revisit Trigger
## Owner
```
