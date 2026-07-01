# Property Search and Verification Workflow

## Goal

Help the user search for real properties, verify available facts, separate assumptions from verified information, and decide whether a property deserves deeper review.

## Operational binding

This workflow must create or update one `properties.cases[]` record per property.

Also update:

- `artifacts`
- `risks`
- `tasks`
- `session`

Typical artifact:

- property intake / property verification report

Typical checkpoints:

- `property_review_done`
- `artifact_updated`
- `red_flag_added`
- `waiting_on_professional`

## Inputs

- Target area.
- Budget range.
- Desired property type.
- Intended use.
- Financing path.
- User constraints.
- Property URL or address.
- Optional screener input when available:
  - `preloaded_state_data`; or
  - `fresh_propwire_export`.

## Search sources

Use browser access where available.

Recommended source order:

1. Listing platform or broker site for initial details.
2. County assessor or property appraiser.
3. County recorder, clerk, or land records.
4. County or city tax collector.
5. City permits and violations portal.
6. FEMA flood maps or local GIS.
7. School district or local municipal source.
8. Comparable sales sources.
9. Rental listing sources if house hacking or investment is relevant.
10. Insurance and climate-risk context sources when available.

## Optional premium deal screener

Use `docs/tools/ownwiseai-deal-screener.md` when the user has access and the screener will change the next action.

Typical triggers:

- many candidate properties need fast triage;
- the user wants a ranked shortlist;
- the property is being evaluated for creative finance, rental, BRRRR, house hack, or small multifamily fit;
- preloaded state data can accelerate first-pass screening;
- a fresh PropWire export is needed because price, DOM, status, or motivation signals must be current.

Do not require the screener for ordinary one-property verification when manual review is already sufficient.

## Screener input rule

Only use these screener inputs as canonical:

1. `preloaded_state_data`
2. `fresh_propwire_export`

For fresh exports, treat `propwire.com` as the standard source with:

- target location;
- `Lead Types: MLS Active`;
- relevant `Property Types`;
- `Owner Type: Individual`.

Do not assume a hand-built spreadsheet is equivalent.

## Verification categories

For each property, verify or flag as unknown:

- address;
- parcel ID;
- owner of record;
- property type;
- legal units versus advertised units;
- beds, baths, square footage;
- lot size;
- year built;
- tax assessment;
- annual property taxes;
- listing status and price history;
- last sale date and amount;
- recorded mortgage clues where public;
- lien or judgment clues where public;
- permits;
- code violations;
- flood zone clues;
- HOA or condo status;
- rental legality if relevant;
- comparable sales;
- estimated rent range;
- repair red flags;
- insurance red flags.

## Screener capture rule

If the screener is used, capture its result separately from verified facts.

Store a compact screening snapshot with:

- source mode;
- source label or dataset scope;
- source checked date;
- primary strategy;
- secondary strategy;
- deal status;
- confidence score;
- risk band;
- suggested offer band;
- seller angle;
- required manual checks.

The screener may guide prioritization, but it does not verify ownership, title, legality, financing approval, or physical condition.

## Output format

```markdown
# Property verification report

## Property
- Address:
- Listing URL:
- Intended strategy:

## Verified facts
| Fact | Value | Source | Date checked |
|---|---|---|---|

## Listing claims
| Claim | Value | Source | Date checked |
|---|---|---|---|

## Estimates
| Estimate | Value/range | Method | Confidence |
|---|---|---|---|

## Unknowns
- ...

## Red flags
- ...

## Questions for professionals
- Buyer agent:
- Lender:
- Inspector:
- Title company:
- Attorney:
- Insurance:

## Strategy fit
- Classic purchase fit:
- Creative finance fit:
- House hack fit:

## Next step
- ...
```

## Russian user-facing rule

When presenting the report to the user, explain it in Russian and clearly label:

- confirmed facts;
- listing claims;
- estimates;
- unknowns;
- professional review items.

## Data quality rule

Do not hide uncertainty. If a source is missing, say what remains unverified.

Operationally:

- store each material fact as an evidence record or mark it unknown;
- store screener outputs as screening outputs rather than verified facts;
- preserve conflicting facts instead of collapsing them;
- set `stale_after` for dynamic items such as listing status, list price, and rent estimates;
- create follow-up tasks for title, permit, flood, insurance, or HOA gaps that block a decision.

## Stop conditions

Recommend pausing deeper work when:

- identity of the property cannot be verified;
- listing has major inconsistencies;
- taxes, legal units, or ownership do not match listing claims;
- visible red flags suggest title, safety, legal, or financing problems;
- user cannot afford the property under conservative assumptions.
