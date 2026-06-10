# Source Registry

## Purpose

The agent already has source-priority rules. This registry adds a repeatable operational map for where to look first by research job type.

It is not an exhaustive state-by-state directory. It is a compact registry of source categories and expected use.

## Core categories

| Category | Typical sources | Use |
|---|---|---|
| Official government | HUD, CFPB, FHA, VA, USDA, FHFA, state housing agency, county assessor, recorder, tax collector, FEMA, municipality | Highest-priority factual verification |
| Official lender / GSE / administrator | lender rate sheets, approved lender lists, program administrator pages, Fannie/Freddie guidance | Loan and program operational details |
| Listing / broker platforms | MLS syndication, broker site, Zillow, Redfin, Realtor | Discovery and listing claims |
| Market-data providers | rent platforms, local market analytics, comp sources | Estimates and context |
| User or professional documents | lender worksheet, pre-approval, HOA packet, seller disclosure, title notes | Case-specific evidence, still requiring source-aware handling |
| General web | articles, blog posts, community references | Discovery only, not final verification |

## Use by workstream

### Property work

1. listing source
2. county assessor
3. recorder / land records
4. tax source
5. permits / violations
6. FEMA / GIS
7. rental and insurance context

### Lender work

1. lender disclosure or lender quote
2. lender website or rate sheet
3. official agency or GSE guidance
4. user-provided notes as temporary inputs

### DPA work

1. state housing agency
2. county or city housing department
3. official program administrator
4. approved lender participation source
5. nonprofit counselor only as secondary support

## Evidence rule

For any fact that changes a decision, store:

- source category;
- source name;
- date checked;
- freshness window;
- classification.
