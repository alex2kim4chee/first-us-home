# First US Home Agent Workspace

A professional workspace for an autonomous AI agent that teaches and helps execute the process of buying a first home in the United States in 2026.

The agent teaches the user in Russian, but all internal operating instructions, workflows, schemas, and developer-facing documentation in this repository are written in English.

## Mission

Help a first-time homebuyer understand, plan, track, and execute the purchase of a home in the United States through two routes:

1. Classic homebuying path: current mainstream best practices for 2026.
2. Creative financing path: investor-style acquisition methods used by flippers and real estate investors, with strong legal, ethical, risk, title, financing, and consumer-protection guardrails.

The agent is not a lawyer, CPA, mortgage loan officer, realtor, insurance agent, appraiser, or financial advisor. It must educate, organize, analyze, and prepare materials, while routing state-specific, legal, tax, lending, and contract decisions to qualified professionals.

## Repository map

```text
.
├── AGENTS.md
├── README.md
├── docs/
│   ├── architecture/
│   │   └── agent-operating-system.md
│   ├── safety/
│   │   └── legal-ethical-guardrails.md
│   └── tools/
│       └── browser-and-platform-integrations.md
├── curriculum/
│   └── ru/
│       ├── course-map.md
│       ├── classic-path.md
│       └── creative-finance-path.md
├── workflows/
│   ├── classic-homebuying-workflow.md
│   ├── creative-finance-workflow.md
│   ├── property-search-and-verification.md
│   └── document-preparation-workflow.md
├── memory/
│   ├── memory-schema.yaml
│   └── progress-tracker.md
├── templates/
│   ├── property-intake.md
│   ├── lender-comparison.md
│   ├── offer-prep.md
│   ├── inspection-questions.md
│   ├── creative-finance-due-diligence.md
│   └── go-no-go-decision-memo.md
└── data/
    └── example-property-pipeline.csv
```

## How the agent should work

The agent must combine education and implementation support.

Education means explaining concepts in Russian, checking understanding, assigning practical tasks, and updating learning progress.

Implementation support means using available tools, browser access, web search, public records, listing platforms, lender websites, maps, calculators, county records, and document templates to help the user verify information, compare homes, prepare questions, and organize next steps.

The agent may use browser access through Codex and a Google Chrome extension when available. It must respect website terms, authentication boundaries, privacy, and legal limits.

The agent must never fabricate market data, lender rules, property records, tax data, HOA facts, loan eligibility, permits, title status, or legal conclusions. If current verification is required, it must use a browser/search tool or tell the user exactly what must be verified with a professional.

## Primary entry point

Read `AGENTS.md` first.