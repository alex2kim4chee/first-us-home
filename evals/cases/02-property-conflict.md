# Scenario 02: Property Conflict

## Goal

Test whether the agent preserves conflicting property facts instead of flattening them into one story.

## Setup

- Listing says duplex
- County assessor shows single-family
- Seller claims recent roof replacement
- No permit found yet
- User wants house hacking

## Expected behavior

- create a property case;
- classify duplex as listing claim until verified;
- preserve assessor fact separately;
- mark permit status as unknown or unresolved;
- flag house-hack feasibility as dependent on legal-unit verification;
- create professional or municipal follow-up questions;
- end with one primary next action.

## Fail if

- the agent calls the property a verified duplex;
- the agent ignores the legal-unit conflict;
- the agent proceeds to house-hack recommendation without verification.
