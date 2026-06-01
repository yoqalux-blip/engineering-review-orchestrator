---
name: engineering-review-orchestrator
description: General engineering review orchestration for codebases, data pipelines, AI/model-assisted reviews, release gates, incident follow-ups, and architecture decisions. Use when Codex needs to turn a messy engineering problem into evidence-backed roles, checks, model-review routing, decision gates, ADR/RFC outputs, or implementation plans.
---

# Engineering Review Orchestrator

## Purpose

Use this skill to coordinate engineering review work across deterministic checks, AI reviewers, human/Codex judgment, and final evidence-based decisions. Prefer it for complex code/data/architecture tasks where the problem needs a review system, not only a quick fix.

## Operating Principle

Separate four things that are often mixed together:

1. **Facts**: source code, data, logs, tests, traces, metrics, contracts, and reproducible commands.
2. **Interpretations**: model findings, reviewer comments, hypotheses, risk ratings, and root-cause theories.
3. **Decisions**: accepted/rejected findings, rule changes, design choices, release gates, and owners.
4. **Actions**: code edits, tests, rollbacks, migrations, docs, tickets, and follow-up audits.

Never let an interpretation bypass evidence. Model consensus is not a decision. A decision requires source evidence, validation, and an owner.

## Review Loop

1. **Frame the problem**
   - State the decision to be made and the blast radius.
   - Classify the work: bug, data quality, security, reliability, architecture, release, incident, or process design.
   - Choose the review mode: fast triage, deep audit, design review, regression gate, or post-incident learning.

2. **Build the evidence packet**
   - Gather only relevant files, diffs, logs, schemas, metrics, sample records, and failing commands.
   - Preserve source paths, line numbers, timestamps, versions, and command outputs.
   - Use `scripts/build_review_packet.py` when a compact packet is useful for another reviewer or model.

3. **Route reviewers**
   - Deterministic tools first: tests, linters, type checks, schema checks, diff checks, reconciliation scripts, benchmarks.
   - Fast/local model or rule-based reviewer for broad repetitive screening.
   - Strong external model for high-risk, uncertain, or disagreement cases.
   - Coding-agent model for cross-file engineering review, method critique, prompt/rule design, and long-context synthesis.
   - Codex or the human owner makes the final decision after validating evidence.

4. **Apply decision gates**
   - Require evidence for every accepted finding.
   - Require a reproduction or deterministic check for every high-impact code/data change.
   - Require rollback or mitigation notes for risky changes.
   - Require ADR/RFC notes for architecture or policy changes.
   - Require explicit manual review when evidence is incomplete.

5. **Close the loop**
   - Implement narrowly.
   - Run the highest-signal checks available.
   - Record what changed, why, evidence used, residual risk, and follow-up owner.

## Reviewer Role Patterns

Use named roles instead of vague "ask another model" language:

- **Deterministic Checker**: executes tests, scripts, reconciliation, parsing, type checks, benchmark comparisons.
- **Bulk Screener**: scans many low/medium-risk items cheaply and produces triage signals.
- **Specialist Reviewer**: reviews high-risk or uncertain cases with deeper domain reasoning.
- **Adversarial Reviewer**: searches for counterexamples, missing evidence, unsafe assumptions, and regression risk.
- **Method Reviewer**: critiques the review process, prompts, sampling, gates, and measurement design.
- **Final Integrator**: accepts/rejects findings and makes local changes after source evidence is verified.

In this workspace, map these roles to available tools/models conservatively. For example, local models handle bulk triage, external APIs handle high-risk row review, coding agents handle engineering/method review, and Codex integrates verified changes.

## Method Stack

Use the minimum method that clarifies the work:

- **PDCA/OODA**: iterate when the problem is moving or evidence is incomplete.
- **DMAIC**: improve a repeated pipeline with measurable defects.
- **FMEA**: list failure modes, severity, occurrence, detection, and controls.
- **RACI/DRI**: assign ownership when multiple reviewers or systems are involved.
- **Cynefin**: decide whether the task is obvious, complicated, complex, or chaotic.
- **Toulmin argument**: separate claim, evidence, warrant, rebuttal, and confidence.
- **MECE / issue tree**: split broad review areas without double-counting.
- **ADR/RFC**: record decisions that change architecture, policy, schema, workflow, or operating rules.
- **Premortem / red team**: search for how the plan could fail before it ships.
- **SRE-style error budget**: balance speed and safety when releases or pipelines are under time pressure.

Read `references/method-stack.md` when choosing a method for a complex or ambiguous task.

## Outputs

Choose the smallest useful output:

- **Triage table**: finding, evidence, severity, owner, next action.
- **Disagreement packet**: source fact, reviewer A, reviewer B, conflict, Codex decision needed.
- **Gate checklist**: required checks before release or data update.
- **ADR/RFC note**: context, options, decision, consequences, rollback.
- **Implementation plan**: scoped edits, validation commands, risks, follow-up.
- **Review packet**: concise context bundle for another model, reviewer, or future Codex turn.

## Resource Guide

- Read `references/reviewer-roles.md` for role assignment and model/tool routing.
- Read `references/decision-gates.md` for acceptance criteria and evidence rules.
- Read `references/method-stack.md` for management, logic, and engineering method selection.
- Run `scripts/build_review_packet.py --help` to create compact Markdown packets from files.
