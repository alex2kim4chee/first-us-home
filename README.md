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
│   │   ├── agent-operating-system.md
│   │   ├── artifact-lifecycle.md
│   │   ├── checkpoint-resume.md
│   │   ├── context-loading-policy.md
│   │   ├── freshness-policy.md
│   │   ├── operator-layer.md
│   │   └── operational-state-model.md
│   ├── quality/
│   │   ├── evaluation-framework.md
│   │   └── failure-modes.md
│   ├── research/
│   │   ├── conflict-resolution.md
│   │   ├── dpa-verification-playbook.md
│   │   ├── lender-comparison-playbook.md
│   │   ├── property-verification-playbook.md
│   │   └── source-registry.md
│   ├── safety/
│   │   └── legal-ethical-guardrails.md
│   └── tools/
│       └── browser-and-platform-integrations.md
├── evals/
│   ├── cases/
│   ├── README.md
│   ├── regression-checklist.md
│   └── scenario-matrix.md
├── curriculum/
│   └── ru/
│       ├── course-map.md
│       ├── learning-experience-model.md
│       ├── classic-path.md
│       └── creative-finance-path.md
├── cases/
│   ├── _case-template.yaml
│   ├── _operator-view-template.yaml
│   └── <case-id>/
├── artifacts/
│   ├── _artifact-manifest-template.yaml
│   └── <case-id>/
├── checkpoints/
│   ├── _checkpoint-template.yaml
│   └── <case-id>/
├── scripts/
│   ├── create_checkpoint.py
│   ├── run_evals.py
│   ├── register_artifact.py
│   ├── scaffold_case.py
│   ├── update_client_case.py
│   ├── update_operator_view.py
│   ├── create-checkpoint.sh
│   ├── register-artifact.sh
│   ├── scaffold-case.sh
│   ├── update-client-case.sh
│   └── update-operator-view.sh
├── workflows/
│   ├── classic-homebuying-workflow.md
│   ├── creative-finance-workflow.md
│   ├── property-search-and-verification.md
│   └── document-preparation-workflow.md
├── memory/
│   ├── client-case-schema.yaml
│   ├── evidence-schema.yaml
│   ├── memory-schema.yaml
│   ├── operator-view-schema.yaml
│   ├── progress-tracker.md
│   ├── session-close-protocol.md
│   └── task-schema.yaml
├── templates/
│   ├── property-intake.md
│   ├── lender-comparison.md
│   ├── offer-prep.md
│   ├── inspection-questions.md
│   ├── creative-finance-due-diligence.md
│   ├── go-no-go-decision-memo.md
│   └── operator-case-snapshot.md
└── data/
    └── example-property-pipeline.csv
```

## How the agent should work

The agent must combine education and implementation support.

Education means explaining concepts in Russian, checking understanding, assigning practical tasks, and updating learning progress.

Implementation support means using available tools, browser access, web search, public records, listing platforms, lender websites, maps, calculators, county records, and document templates to help the user verify information, compare homes, prepare questions, and organize next steps.

The agent may use browser access through Codex and a Google Chrome extension when available. It must respect website terms, authentication boundaries, privacy, and legal limits.

The agent must never fabricate market data, lender rules, property records, tax data, HOA facts, loan eligibility, permits, title status, or legal conclusions. If current verification is required, it must use a browser/search tool or tell the user exactly what must be verified with a professional.

Operationally, the repository now treats each user as a long-running case with:

- canonical state;
- evidence records with freshness;
- task queue;
- versioned artifacts;
- thin operator cockpit;
- checkpoint/resume lifecycle.

Runtime-wise, the repository now also includes a file-based layout for:

- active cases;
- operator views;
- artifact manifests;
- immutable checkpoints.

Quality-wise, the repository now also includes:

- an evaluation framework;
- named failure modes;
- a scenario matrix;
- regression cases for live buyer-support behavior.

The repository also includes a cross-platform eval runner that turns scenario cases into a structured markdown scoring report.

## Primary entry point

Read `AGENTS.md` first, then:

1. `docs/architecture/operational-state-model.md`
2. `docs/architecture/checkpoint-resume.md`
3. `docs/architecture/freshness-policy.md`
4. `docs/architecture/artifact-lifecycle.md`
5. `docs/architecture/operator-layer.md`
6. `docs/architecture/context-loading-policy.md`
7. `docs/quality/evaluation-framework.md`
8. `docs/research/source-registry.md`
9. `docs/runtime/file-runtime.md`
10. `curriculum/ru/learning-experience-model.md`
