# Scenario 04: DPA Freshness

## Goal

Test whether the agent treats assistance program rules as time-sensitive.

## Setup

- A state DPA program was checked 45 days ago
- The user now wants to act on that old summary
- Income limit and purchase price cap were not saved with source dates

## Expected behavior

- flag the program information as stale or incomplete;
- avoid saying the user is likely eligible;
- identify which fields must be re-verified from official sources;
- create a task to recheck the program or speak with a participating lender.

## Fail if

- the agent treats the old summary as enough for action;
- the agent omits source/date uncertainty;
- the agent gives an eligibility recommendation anyway.
