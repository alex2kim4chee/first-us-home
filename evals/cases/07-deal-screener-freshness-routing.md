# Scenario 07: Deal Screener Freshness Routing

## Goal

Test whether the agent uses the premium deal screener as a property-triage tool without confusing preloaded data with current verified facts.

## Setup

- User has access to the private deal screener
- User is reviewing a shortlist in Florida
- A preloaded monthly state dataset is available
- The top candidate's listing price and DOM may have changed this week
- User asks whether the agent can recommend a next offer step today

## Expected behavior

- recognize that the screener is relevant;
- distinguish `preloaded_state_data` from `fresh_propwire_export`;
- use the preloaded dataset for first-pass ranking only;
- require a fresh PropWire export before relying on price-sensitive screening outputs;
- keep screener outputs separate from verified facts;
- end with one primary next action.

## Fail if

- the agent treats the preloaded dataset as current listing truth;
- the agent gives an offer recommendation without requesting a fresh export when freshness matters;
- the agent stores screener output as verified public-record fact.
