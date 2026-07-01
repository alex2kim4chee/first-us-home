# Scenario 08: Classic Buyer Screening Boundary

## Goal

Test whether the agent avoids overusing investor-style screening for a standard first-home buyer when it would not change the immediate next action.

## Setup

- User is a classic-path first-time buyer
- User is looking at one owner-occupied single-family home to live in
- User needs help understanding taxes, insurance, commute, and lender fit
- User has no active premium screener task running

## Expected behavior

- keep the main workflow on property verification and affordability;
- avoid making the deal screener the center of the turn;
- explain that the screener is optional and not required for this step;
- preserve classic-path priorities such as lender fit, payment comfort, and verification;
- end with one primary next action.

## Fail if

- the agent forces investor-style screening as the main next step;
- the agent ignores affordability or verification questions;
- the agent frames the property mainly as a flip or creative-finance opportunity without user need.
