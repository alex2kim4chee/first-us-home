# Freshness Policy

## Purpose

Many critical homebuying facts change quickly. The agent must not treat old data as current just because it was once verified.

Use `memory/evidence-schema.yaml` for all material facts that need source and freshness metadata.

## Core rule

Every material fact should be handled as:

- claim;
- source;
- date checked;
- freshness window;
- confidence;
- stale status.

## Default freshness windows

Use the shortest practical window unless a better source-specific window is known.

| Category | Examples | Freshness window |
|---|---|---:|
| Very short-lived | active listing status, list price, lender quote, rate lock details | 1-7 days |
| Short-lived | DPA rules, approved lender lists, program overlays, rent listings | 30 days |
| Medium-lived | assessor ownership snapshot, tax amounts, permit status, HOA summary notes | 90 days |
| User-stable | employment type, intended use, risk tolerance, timeline | until changed |
| Calculation-derived | affordability estimate, cash-to-close estimate, DTI estimate | stale when any input changes |

## Stale handling

When a record is stale:

1. do not present it as current without a warning;
2. mark the related subject as needing recheck;
3. create a verification task if the stale fact blocks a decision;
4. prefer official re-verification when available.

## Confidence rule

Freshness does not equal confidence.

Examples:

- a fresh listing fact may still be a `listing_claim`;
- an older assessor record may still be high-confidence for historical ownership;
- a user-reported lender rate is fresh but still `user_provided` until documented.

## Input change rule

Recompute dependent estimates when any of these change:

- purchase price;
- down payment plan;
- rate;
- taxes;
- insurance estimate;
- HOA dues;
- debt obligations;
- household income assumptions.

## Blocking decisions

The following should trigger caution if stale or unknown:

- lender quote used for comparison;
- DPA program used for action planning;
- property taxes used in affordability;
- flood or insurance clues used for go/no-go;
- title or lien clues used for creative finance analysis.

## User-facing communication rule

In Russian, the agent should explicitly say when something is:

- confirmed and current;
- confirmed but stale;
- a listing claim;
- an estimate;
- still unknown.
