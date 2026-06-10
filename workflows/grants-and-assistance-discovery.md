# Grants and Assistance Discovery Workflow

## Goal

Help the user discover, understand, compare, and prepare for first-time buyer grants, down payment assistance, tax credits, forgivable loans, deferred-payment assistance, and state/local incentives.

This workflow is part of the classic path, but it may also support house hacking and some creative finance planning when a program allows it.

The learner-facing explanation must be in Russian.

## Operational binding

This workflow must update:

- `assistance_programs.programs`
- `financial_snapshot`
- `lenders`
- `artifacts`
- `tasks`
- `session`

Typical artifact:

- assistance program comparison table

Typical checkpoints:

- `dpa_shortlist_updated`
- `artifact_updated`
- `waiting_on_user`
- `waiting_on_professional`

## Core learner promise

Many first-time buyers assume they must save 20 percent before buying a home. The agent must teach that this is often not the only path, but it must avoid promising eligibility, approval, or free money.

The correct message is:

```text
You may not need 20 percent down, but every program has rules. The agent helps identify programs to research, compare requirements, prepare questions, and organize the application path.
```

## When to run this workflow

Run this workflow when:

- the user is a first-time buyer;
- the user asks about affordability;
- the user believes 20 percent down is required;
- the user has limited cash for down payment or closing costs;
- the user is comparing FHA, conventional, VA, USDA, or state programs;
- the user provides a target state, county, or city;
- the user wants a practical plan to reduce upfront cash needs;
- the user asks about grants, DPA, tax credits, closing cost help, or state programs.

## Required inputs

Collect safe summaries only:

- target state;
- target county and city;
- intended use: primary residence, house hack, investment;
- first-time buyer status;
- income range;
- household size;
- military/veteran status if user chooses to share;
- profession category if relevant: teacher, nurse, first responder, public employee, etc.;
- credit score range;
- purchase price range;
- available cash range;
- preferred loan type if known;
- whether the user has completed homebuyer education;
- whether the user already has a lender.

Do not request sensitive documents unless the user is preparing for a professional application. Do not store sensitive raw documents.

State updates:

- write user fit assumptions into the case as safe summaries only;
- create tasks for missing eligibility inputs such as county, household size, or target price.

## Program categories to research

### Federal and national categories

- FHA-compatible assistance;
- VA-related home loan benefits if eligible;
- USDA eligibility in qualifying areas;
- Fannie Mae and Freddie Mac low down payment programs;
- HUD homebuyer resources;
- Good Neighbor Next Door when applicable;
- homebuyer education programs.

### State programs

Research the state housing finance agency.

Look for:

- down payment assistance grants;
- forgivable second loans;
- deferred-payment second loans;
- low-interest second loans;
- closing cost assistance;
- mortgage credit certificates if available;
- first-time buyer mortgage products;
- income and purchase price limits;
- approved lender lists;
- homebuyer education requirements.

### County and city programs

Research local programs for:

- city grants;
- county assistance;
- neighborhood revitalization programs;
- first-generation buyer programs;
- employer-assisted housing partnerships;
- targeted census tract programs;
- closing cost help.

### Employer and profession-based programs

Research or ask the user to verify:

- employer housing assistance;
- union benefits;
- teacher programs;
- nurse or healthcare worker programs;
- first responder programs;
- public employee programs;
- military and veteran programs.

## Browser/source priority

Use current sources. Program rules change often.

Priority order:

1. Official state housing finance agency.
2. Official city or county housing department.
3. HUD or other federal agency pages.
4. Official program administrator.
5. Approved lender list or lender-published program sheet.
6. Reputable nonprofit housing counseling agency.
7. General articles only for discovery, not final eligibility.

Operational rule:

- every material program field must be stored as evidence with source, date checked, and freshness;
- expired program checks should become stale and trigger re-verification before the agent relies on them.

## What to capture for each program

```yaml
assistance_program:
  program_name: null
  jurisdiction: federal | state | county | city | employer | nonprofit | lender
  source_url: null
  date_checked: null
  assistance_type: grant | forgivable_loan | deferred_loan | low_interest_second | tax_credit | closing_cost_help | education | other
  max_amount_or_range: null
  repayment_required: unknown
  forgiveness_terms: null
  income_limits: null
  purchase_price_limits: null
  location_limits: null
  property_type_limits: null
  occupancy_requirement: null
  first_time_buyer_requirement: null
  credit_score_requirement: null
  debt_to_income_requirement: null
  approved_lender_required: unknown
  homebuyer_education_required: unknown
  can_combine_with_fha: unknown
  can_combine_with_conventional: unknown
  can_combine_with_va: unknown
  can_combine_with_usda: unknown
  estimated_fit_for_user: unknown
  missing_info: []
  questions_for_lender_or_program_admin: []
```

## Output format

The user-facing output must be in Russian:

```markdown
## Программы помощи для первого покупателя

### Главное
Вы не обязаны автоматически копить 20%, но нужно проверить программы по вашему штату, county, income, цене дома и типу кредита.

### Найденные программы
| Program | Type | Possible help | Repayment? | Key requirements | Fit |
|---|---|---:|---|---|---|

### Что выглядит перспективно
- ...

### Что может не подойти
- ...

### Что нужно проверить с lender / program admin
- ...

### Документы, которые могут понадобиться
- ...

### Следующий шаг
- ...
```

## Eligibility language

Do not say:

- you qualify;
- you will receive;
- guaranteed grant;
- free money;
- no down payment needed;
- approval is likely.

Say:

- may be worth checking;
- potential fit;
- eligibility must be confirmed;
- lender or program administrator must verify;
- rules may depend on county, income, price, and loan type.

## Integration with lender comparison

For each lender quote, ask:

- Does this lender participate in the program?
- Can the program be combined with this loan type?
- Does the assistance affect the rate?
- Is it a grant, forgivable loan, deferred loan, or second mortgage?
- What are the repayment or recapture rules?
- Is homebuyer education required?
- What is the application timeline?
- Can seller credits be combined with assistance?

## Integration with property search

For each property, check:

- whether the property location is eligible;
- whether purchase price is within limits;
- whether property type is allowed;
- whether occupancy requirements match user intent;
- whether assistance timeline fits offer/closing timeline.

## Red flags

Mark red flags when:

- a source claims guaranteed free money;
- a program asks for upfront fees before eligibility review;
- a program is not traceable to an official or reputable source;
- the assistance is actually a loan but marketed as a grant;
- repayment terms are unclear;
- the program cannot be combined with the user's likely loan;
- the timeline is too slow for the target closing date;
- income or purchase price limits appear likely to disqualify the user.

## Completion criteria

This workflow is complete when the agent has:

- identified relevant federal/state/local/employer categories;
- created a program comparison table;
- marked potential fit and missing information;
- prepared lender/program-admin questions;
- updated the progress tracker;
- saved next actions in memory.
