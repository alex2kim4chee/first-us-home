# Common Failure Modes

## Purpose

This document defines the most important ways the agent can fail in real long-running buyer support.

Use it during review and regression testing.

## Failure mode list

## 1. Case reset failure

The agent behaves as if prior intake, property work, or lender work never happened.

Signals:

- asks for the same intake again without reason;
- ignores open tasks;
- loses active property or active lender comparison;
- restarts the workflow at module 0 when it should resume.

## 2. Evidence collapse

The agent merges listing claims, user claims, and verified facts into one undifferentiated summary.

Signals:

- presents listing data as verified without attribution;
- omits source/date for material claims;
- hides conflicts between sources.

## 3. Freshness failure

The agent treats old dynamic facts as current.

Signals:

- old rate quote used for current comparison with no warning;
- old DPA rule treated as actionable;
- stale list price or status used for a property decision.

## 4. Task drift

The agent ends with vague advice instead of actionable case progression.

Signals:

- multiple unfocused next steps;
- no clear primary next action;
- waiting items are forgotten;
- blockers are described but not tracked.

## 5. Safety gate miss

The agent fails to stop or reroute a risky move.

Signals:

- subject-to treated casually;
- user encouraged to hide facts from lender or insurer;
- title, inspection, or insurance review treated as optional without consequences;
- legal conclusions stated as final.

## 6. Educational verbosity without operational value

The agent gives long explanations but does not improve the case state.

Signals:

- no artifact update;
- no task update;
- no risk update;
- no change in user readiness despite a long answer.

## 7. Artifact fragmentation

The agent recreates the same document repeatedly instead of updating one working artifact.

Signals:

- multiple versions with no linkage;
- property report rewritten from scratch every time;
- lender comparison duplicated instead of revised.

## Reviewer rule

When one of these failures appears, log:

- the scenario;
- the failing dimension;
- the first observable symptom;
- the likely missing instruction or schema discipline.
