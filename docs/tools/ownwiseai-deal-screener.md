# OwnWiseAI Deal Screener

## Purpose

Define how the agent should use the private premium deal screener without turning it into a second brain or a replacement for verification.

This is an optional operator tool for paid users who have access to the screener on the seller's platform.

## Core role

The screener is a deterministic property-screening layer.

It helps the agent:

- rank and triage multiple candidate properties;
- identify the most plausible acquisition strategy;
- estimate a screening-grade offer band;
- surface red flags and manual checks before deeper work;
- accelerate shortlist creation for house hack, rental, BRRRR, and creative-finance style reviews.

It does not replace:

- lender underwriting;
- title review;
- attorney review;
- inspection;
- insurance review;
- final comp analysis;
- DPA eligibility verification;
- official property verification from public records.

## Access rule

The agent does not provision, manage, or troubleshoot product access.

Canonical screener URL:

- `https://screener.ownwiseai.com/`

If the user has access, the agent may guide them in using the screener and interpreting results.

If the user does not have access, continue with the normal repository workflows instead of blocking progress.

## User handoff rule

When the user needs to open the tool, direct them to:

- `https://screener.ownwiseai.com/`

Use simple Russian guidance such as:

```text
Откройте скринер по адресу https://screener.ownwiseai.com/. Если нужен самый актуальный screening по объектам, загрузите свежий export из PropWire. Если нужен быстрый первый проход, можно начать с preloaded state data.
```

## Approved input modes

The agent should only treat these two inputs as canonical:

1. `preloaded_state_data`
2. `fresh_propwire_export`

Do not treat arbitrary spreadsheets or hand-built CSVs as equivalent unless the tool itself explicitly accepts them and the user confirms the source.

## Fresh PropWire export standard

When the user needs current screening data, the canonical source is a fresh export from `propwire.com`.

Required filter recipe:

- target location;
- `Lead Types: MLS Active`;
- relevant `Property Types`;
- `Owner Type: Individual`.

The user may use a free PropWire account for this workflow.

## Preloaded dataset rule

Preloaded state datasets are useful for fast triage and education, especially in states commonly used by the Russian-speaking community.

Treat them as:

- screening-grade;
- strategic;
- potentially stale for price-sensitive decisions.

If the next recommendation depends on current listing status, current list price, current DOM, or current seller-motivation clues, prefer `fresh_propwire_export`.

## When to use the screener

Use it when the user needs:

- ranking across many properties;
- a first shortlist;
- strategy comparison across the same candidate set;
- quick triage for creative finance, house hack, rental, BRRRR, or small multifamily opportunities;
- a screening output before deeper manual verification.

## When not to make it the primary tool

Do not make the screener the primary engine when:

- the user is only learning a concept with no active properties;
- the task is lender comparison;
- the task is DPA research;
- the task is title, permit, flood, insurance, or legal verification;
- the user is a standard classic-path buyer reviewing one property and the screener would not change the next action.

The screener should support the property workflow, not replace it.

## Output contract

The agent may use the screener to interpret or capture these fields:

- `primary strategy`
- `secondary strategy`
- `deal status`
- `confidence score`
- `risk band`
- `suggested offer band`
- `seller angle`
- `red flags`
- `required manual checks`

Treat these as screening outputs, not as verified facts.

## State and artifact mapping

When screener results affect a live case, store them as a compact `screening_snapshot` under the relevant property case.

Also mirror the relevant conclusions into:

- the property intake / verification artifact; or
- the go / no-go memo when the property is already under deeper review.

Do not overwrite verified facts with screener assumptions.

Verified facts stay in:

- `verified_facts`
- `listing_claims`
- `estimates`
- `unknowns`

The screener snapshot is an operator aid, not a source-of-truth replacement.

## Russian user-facing rule

Explain screener results in Russian.

When useful, keep the English term and add a Russian explanation, for example:

```text
Primary strategy — это наиболее подходящий сценарий сделки по текущим данным скринера.
```

The user-facing explanation should always separate:

- what the screener suggests;
- what is verified;
- what still requires manual or professional review.

## Safety rule

The agent must never treat screener output as proof that:

- a property is safe to buy;
- title is clear;
- creative finance is compliant or safe;
- the user qualifies for financing;
- a suggested offer band is appropriate without rechecking stale data.

If the screener points toward creative finance, the normal creative-finance safety gates still apply.

## Minimal operating pattern

1. Decide whether screening will change the next action.
2. Confirm the input mode: `preloaded_state_data` or `fresh_propwire_export`.
3. Capture the screener summary.
4. Explain the result in Russian.
5. Separate screening output from verified facts.
6. Create or update the property artifact.
7. Create follow-up tasks for title, permit, insurance, lender, or legal checks as needed.
8. End with one primary next action.
