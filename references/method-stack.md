# Method Stack

Use methods as lightweight thinking tools, not ceremony. Pick one or two that reduce ambiguity.

## PDCA / OODA

Use for iterative work where new evidence changes the plan.

- Plan / Observe: define the question and collect evidence.
- Do / Orient: make the smallest useful intervention.
- Check / Decide: compare against expected results.
- Act: standardize the improvement or revise the hypothesis.

Good for: prompt tuning, parser repair, CI flake reduction, audit-loop improvement.

## DMAIC

Use when a repeated process has measurable defects.

- Define: defect type and affected workflow.
- Measure: baseline counts, rates, examples.
- Analyze: root causes and segmentation.
- Improve: targeted change.
- Control: regression checks and monitoring.

Good for: data quality pipelines, ingestion failures, review backlog reduction.

## FMEA

Use before risky changes.

Table columns:

- Function or step
- Failure mode
- Effect
- Cause
- Existing control
- Severity
- Occurrence
- Detection
- Mitigation

Good for: migrations, parser changes, release gates, clinical/research asset transformations, payment/security changes.

## RACI / DRI

Use when responsibility is unclear.

- Responsible: does the work.
- Accountable / DRI: owns the decision.
- Consulted: provides evidence or expertise.
- Informed: needs the result.

Good for: multi-reviewer workflows, model-assisted triage, production rollout, incident follow-up.

## Cynefin

Use to pick the operating mode.

- Obvious: apply known rule/checklist.
- Complicated: analyze with expert review.
- Complex: run probes, compare outcomes, iterate.
- Chaotic: stabilize first, defer optimization.

Good for: deciding whether to script, ask a specialist, experiment, or pause for containment.

## Toulmin Argument

Use for review decisions.

- Claim: what is asserted.
- Evidence: source facts.
- Warrant: why evidence supports the claim.
- Rebuttal: what could make it false.
- Qualifier: confidence and scope.

Good for: accepting/rejecting model findings, ADRs, root-cause claims, security reviews.

## MECE / Issue Tree

Use to decompose broad reviews.

- Split by subsystem, data lifecycle, failure mode, or user journey.
- Avoid overlapping buckets.
- Add an "unknown/other" bucket only as a temporary escape hatch.

Good for: large codebase audits, data lineage reviews, architecture reviews.

## ADR / RFC

Use when a decision changes architecture, schema, interface, policy, or operating rules.

Minimum fields:

- Context
- Decision
- Options considered
- Evidence
- Consequences
- Rollback or migration
- Owner and review date

## Premortem / Red Team

Use before shipping risky work.

Ask:

- How could this fail silently?
- What evidence would we wish we had?
- What assumption is most fragile?
- What is the cheapest detection control?

## SRE Error Budget

Use when speed and safety conflict.

- Define the reliability target or acceptable defect rate.
- Compare current risk against remaining budget.
- If budget is burned, prefer stabilization and controls over feature velocity.
