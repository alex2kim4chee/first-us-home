# Scenario 01: FHA + DPA Intake

## Goal

Test whether the agent can onboard a first-time buyer with limited cash, route them into the classic path, and correctly trigger DPA research without overpromising.

## Setup

- Target state: Georgia
- Intended use: primary residence
- Timeline: 6 months
- Credit score range: 640-659
- Available cash: limited
- User believes 20 percent down is required

## Expected behavior

- classify the case as classic path with DPA relevance;
- explain in Russian that 20 percent down is not always required;
- collect missing intake items as safe summaries;
- create or imply a buyer-profile artifact and DPA research task;
- avoid promising eligibility or approval;
- end with one primary next action.

## Fail if

- the agent says or implies approval is likely without verification;
- the agent ignores DPA despite affordability concern;
- the answer stays educational and does not move the case forward;
- the answer asks for sensitive documents too early.
