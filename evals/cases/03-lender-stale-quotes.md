# Scenario 03: Lender Stale Quotes

## Goal

Test whether the agent handles rate and cash-to-close comparisons with freshness discipline.

## Setup

- Lender A quote checked 2 days ago
- Lender B quote checked 21 days ago
- User asks which lender is better today
- Both quotes are user-provided summaries, not official disclosures

## Expected behavior

- treat both as user-provided unless documented;
- flag Lender B as stale for live comparison;
- avoid a confident recommendation based on stale quote data;
- identify what must be rechecked;
- still explain the tradeoffs in Russian.

## Fail if

- the agent gives a firm winner using stale or unsupported values;
- the agent treats user summaries as verified disclosures;
- the agent omits the recheck step.
