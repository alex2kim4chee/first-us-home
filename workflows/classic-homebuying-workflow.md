# Classic Homebuying Workflow

## Goal

Guide a first-time buyer through the standard U.S. home purchase process while teaching the user in Russian and turning each lesson into practical work.

## Operational binding

This workflow must update the canonical case state in `memory/client-case-schema.yaml`.

Primary sections touched by this workflow:

- `profile`
- `learning`
- `execution`
- `financial_snapshot`
- `professionals`
- `properties`
- `lenders`
- `assistance_programs`
- `artifacts`
- `tasks`
- `session`

Typical artifacts created or updated:

- buyer readiness profile
- lender comparison
- assistance program comparison
- property intake
- offer preparation memo

Typical checkpoints:

- `buyer_intake_updated`
- `lesson_done`
- `lender_compare_updated`
- `property_review_done`
- `artifact_updated`
- `waiting_on_user`

## Phase 0: Buyer intake

Collect a safe summary of:

- target state, city, and county;
- intended use: primary residence, house hack, or investment;
- employment type;
- income range;
- credit score range;
- available cash range;
- comfortable monthly payment;
- major monthly debt payments;
- timeline;
- preferred property type;
- risk tolerance.

Output:

- buyer readiness profile;
- missing information list;
- first 30-day plan.

State updates:

- update `profile`;
- set `execution.readiness_status` to `in_progress`;
- create or update a buyer profile artifact;
- open tasks for missing intake items.

## Phase 1: Financial readiness

Teach in Russian:

- credit score;
- debt-to-income ratio;
- income documentation;
- asset documentation;
- cash to close;
- reserves;
- down payment;
- closing costs;
- comfortable payment versus maximum approval.

Implementation support:

- build rough affordability estimate;
- create document collection checklist;
- identify likely loan categories;
- identify state and local assistance programs;
- prepare questions for lenders.

State updates:

- update `financial_snapshot`;
- create evidence-backed affordability assumptions where possible;
- open lender research tasks;
- open assistance-program research tasks if affordability is a concern.

## Phase 2: Lender comparison

Support the user in comparing multiple lenders.

Track:

- rate;
- APR;
- points;
- lender fees;
- estimated monthly payment;
- estimated cash to close;
- mortgage insurance if applicable;
- lock period;
- loan program;
- required documents;
- conditions and open questions.

Output:

- lender comparison table;
- questions to ask each lender;
- Russian explanation of the tradeoffs.

State updates:

- update `lenders.quotes`;
- attach evidence records to quote fields when sourced;
- mark stale lender quotes for recheck;
- set one primary next action tied to the best unresolved comparison step.

## Phase 3: Homebuying team

Help the user understand and interview:

- buyer agent;
- attorney when needed or customary;
- inspector;
- insurance professional;
- title or settlement company;
- contractor when repair estimates are needed.

Output:

- interview questions;
- professional contact tracker;
- role explanations in Russian.

State updates:

- update `professionals`;
- open `waiting_user` or `follow_up` tasks for outreach;
- capture missing professional-review dependencies for active properties or offers.

## Phase 4: Property search

For each candidate property, create a property intake record.

Capture:

- address;
- listing price;
- property type;
- beds, baths, square feet;
- lot size;
- year built;
- taxes;
- HOA or condo fee if any;
- listing history;
- comparable sales;
- repair flags;
- commute and neighborhood notes;
- financing fit;
- open questions.

Use browser tools to verify current and local facts when available.

State updates:

- create or update a `properties.cases[]` record for each candidate;
- classify facts as verified, listing claim, estimate, or unknown;
- create evidence records for taxes, ownership, price history, and other material facts;
- create a property artifact instead of rewriting the case from scratch.

## Phase 5: Offer preparation

Teach the user in Russian how offers work.

Prepare:

- offer price logic;
- deposit explanation;
- financing protection points;
- appraisal-related questions;
- inspection-related questions;
- title-related questions;
- seller credit strategy;
- closing date considerations;
- repair credit strategy.

Output:

- offer preparation memo;
- questions for the real estate professional or attorney;
- risk-adjusted offer notes.

## Phase 6: Under contract tracker

Track:

- contract date;
- deposit deadline;
- inspection deadline;
- financing milestones;
- appraisal status;
- title review status;
- insurance status;
- final walk-through;
- closing date.

Output:

- milestone tracker;
- inspection questions;
- title questions;
- closing checklist.

## Phase 7: Closing preparation

Teach:

- closing disclosure basics;
- cash-to-close review;
- final walk-through;
- closing day expectations;
- post-closing setup.

Output:

- closing readiness checklist;
- final walk-through checklist;
- first 90 days of ownership checklist.

## Completion criteria

This workflow is complete when the user has:

- bought a home; or
- paused with a documented reason; or
- completed readiness preparation and has a clear next-step plan.
