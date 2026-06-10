# Browser and Platform Integrations

## Purpose

The agent may use browser access, including a Codex Google Chrome extension, to help the user research, verify, organize, and prepare a real homebuying process.

The agent must respect website terms, authentication boundaries, privacy, and legal limits.

Operational references:

- `docs/research/source-registry.md`
- `docs/research/conflict-resolution.md`
- `docs/research/property-verification-playbook.md`
- `docs/research/lender-comparison-playbook.md`
- `docs/research/dpa-verification-playbook.md`

## Browser use cases

Use browser workflows for:

- property listing research;
- comparable sales research;
- property tax lookup;
- public assessor records;
- recorder of deeds / land records;
- permits and code violations;
- flood maps;
- school district confirmation;
- commute checks;
- insurance risk indicators;
- lender program and rate research;
- FHA/VA/USDA/Fannie/Freddie/FHFA/HUD/CFPB guidance;
- state housing finance agency programs;
- county and municipal requirements;
- HOA or condo document discovery when public;
- rent estimates and local rental licensing research.

## Common platforms and expected outputs

| Platform type | Examples | Purpose | Output |
|---|---|---|---|
| Listing platforms | Zillow, Redfin, Realtor, Homes, local broker sites | Identify candidate homes and listing details | Property intake record |
| County assessor | County property appraiser / assessor | Verify parcel, owner, assessment, taxes | Tax and identity facts |
| Recorder / land records | Recorder of deeds, clerk, land records | Identify deeds, mortgages, liens where public | Title-risk notes, not final title opinion |
| Municipal portals | City permits, violations, licenses | Check permits, open violations, rental licensing | Permit/violation notes |
| Federal sources | HUD, FHA, FHFA, CFPB, VA, USDA | Verify program rules and limits | Program notes with source/date |
| State sources | State housing finance agency | Down payment assistance and grants | DPA shortlist |
| Maps | Google Maps, FEMA, county GIS | Commute, flood, parcel context | Map notes |
| Rent data | Zillow rent, Rentometer, Apartments, local listings | Estimate house-hack/investment income | Rent range estimate |
| Insurance context | FEMA, state insurance resources, carrier quotes if user obtains them | Risk indicators | Insurance questions |

## Data capture standard

Every researched property should produce a structured record:

```yaml
property_record:
  address: null
  parcel_id: null
  source_urls: []
  listing_price: null
  listing_status: null
  property_type: null
  beds_baths_sqft: null
  lot_size: null
  year_built: null
  taxes_current_year: null
  assessed_value: null
  owner_of_record: null
  last_sale: null
  mortgage_or_lien_clues: []
  permit_clues: []
  violation_clues: []
  flood_zone_clues: []
  hoa_or_condo_clues: []
  insurance_risk_clues: []
  comps_summary: null
  rent_estimate_range: null
  financing_fit: null
  creative_finance_fit: null
  open_questions: []
  professional_reviews_needed: []
```

## Verification standard

Do not state a property fact as verified unless the source supports it.

Use labels:

- `verified`: supported by official or direct source;
- `listing_claim`: stated by a listing platform or seller;
- `estimate`: calculated or source-derived estimate;
- `user_provided`: provided by the user;
- `unknown`: not yet verified.

## External account access

If the platform requires login, payment, or private user data:

- ask the user to log in directly;
- do not ask for passwords;
- do not scrape private data;
- do not bypass access controls;
- summarize only what the user authorizes or provides.

## Browser workflow pattern

1. Define the research question.
2. Identify source priority.
3. Search or open sources.
4. Capture facts with source and date.
5. Mark unknowns.
6. Convert findings into a user-facing Russian explanation.
7. Update the property pipeline and progress tracker.
8. Create the next action list.

## Example Russian user-facing summary

```text
Я проверил объект по трем типам источников: listing, county assessor и flood map. Цена и характеристики пока считаются listing_claim, налоги подтверждены county assessor, flood risk требует дополнительной проверки через insurance quote. Следующий шаг — запросить seller disclosure, HOA documents и получить предварительный insurance estimate.
```
