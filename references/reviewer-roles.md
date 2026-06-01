# Reviewer Roles

Assign roles by capability and failure mode. Avoid using the strongest model for every task.

## Deterministic Checker

Use for facts and reproducibility.

Examples:

- unit/integration tests
- linters and type checks
- schema validation
- row-count reconciliation
- checksum/diff checks
- benchmarks

Trust level: highest for what it directly measures, low outside its measurement scope.

## Bulk Screener

Use for high-volume low/medium-risk triage.

Good tasks:

- classify many similar records
- identify likely false positives
- produce confidence/risk labels
- route uncertain items upward

Do not allow bulk screener output to directly change source data or final decisions.

## Specialist Reviewer

Use for high-risk or uncertain cases.

Good tasks:

- P0/P1/P2 issues
- low confidence or contradictory evidence
- ambiguous domain semantics
- examples where deterministic checks disagree with bulk screening

Require source evidence and a final integrator decision.

## Adversarial Reviewer

Use before risky changes.

Good tasks:

- search for counterexamples
- inspect edge cases
- challenge root-cause claims
- find hidden regression paths
- review rollback plans

Ask for concrete failure scenarios, not generic warnings.

## Method Reviewer

Use for process quality.

Good tasks:

- audit routing rules
- prompt/schema regression analysis
- sampling bias review
- cross-round synthesis
- traceability gap detection
- review of gates and acceptance criteria

Coding-agent models are often strong here because they can inspect files, scripts, diffs, and reports.

## Final Integrator

Use for decisions and changes.

Responsibilities:

- verify evidence
- accept/reject findings
- implement scoped edits
- run validation
- record residual risk

In Codex workflows, Codex usually acts as final integrator unless the user explicitly assigns that role to a human.

## Routing Heuristics

- Send repetitive queue-shaped work to a bulk screener.
- Send rare/high-risk/uncertain work to a specialist reviewer.
- Send process, prompt, schema, and cross-file review to a method reviewer.
- Send format failures to method review first; they are often prompt/schema faults.
- Resolve disagreements by evidence, not majority vote.
- Bundle final review by source file, trace, subsystem, or ownership boundary.
