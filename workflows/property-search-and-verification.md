# Property Search and Verification Workflow

## Goal

Help the user search for real properties, verify available facts, separate assumptions from verified information, and decide whether a property deserves deeper review.

## Inputs

- Target area.
- Budget range.
- Desired property type.
- Intended use.
- Financing path.
- User constraints.
- Property URL or address.

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

## Stop conditions

Recommend pausing deeper work when:

- identity of the property cannot be verified;
- listing has major inconsistencies;
- taxes, legal units, or ownership do not match listing claims;
- visible red flags suggest title, safety, legal, or financing problems;
- user cannot afford the property under conservative assumptions.
