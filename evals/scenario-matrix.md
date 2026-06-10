# Scenario Matrix

## Purpose

This matrix defines the minimum set of regression scenarios for the repository.

| Scenario | Focus | Type | Priority |
|---|---|---|---|
| 01-fha-dpa-intake | intake, affordability, DPA routing | multi-turn | high |
| 02-property-conflict | conflicting property facts, evidence discipline | multi-turn | high |
| 03-lender-stale-quotes | stale rate handling, comparison discipline | multi-turn | high |
| 04-dpa-freshness | stale program data and eligibility caution | multi-turn | high |
| 05-subject-to-risk | creative finance safety gate | multi-turn | critical |
| 06-pause-resume-topic-switch | state continuity across time and topic switches | multi-turn | high |

## Release gate

Do not consider the agent stable for real-user use unless all high and critical scenarios pass.
