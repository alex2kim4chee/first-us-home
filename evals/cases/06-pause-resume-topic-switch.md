# Scenario 06: Pause, Resume, Topic Switch

## Goal

Test whether the agent can preserve continuity across time and topic changes.

## Setup

Session 1:
- buyer intake mostly complete
- active property under review
- two open lender questions

Session 2 after 3 weeks:
- user asks about DPA instead of the property

Session 3:
- user returns to the original property

## Expected behavior

- checkpoint the first branch;
- handle DPA without deleting property/lender context;
- on return, resume the property branch with stale-item awareness;
- preserve open lender questions and active property tasks;
- avoid restarting the whole case from intake.

## Fail if

- the agent forgets the property branch;
- the agent loses open lender items;
- the agent resumes with no awareness that dynamic facts may now be stale.
