# Eval Runner

Use the cross-platform runner:

```text
python scripts/run_evals.py list
python scripts/run_evals.py report
python scripts/run_evals.py report 05-subject-to-risk
python scripts/run_evals.py report -o evals/reports/latest.md
```

Windows alternative:

```text
py -3 scripts\run_evals.py list
py -3 scripts\run_evals.py report
```

What it does:

- reads `evals/scenario-matrix.md`
- loads matching files from `evals/cases/`
- generates a structured markdown report template for scoring

What it does not do:

- it does not run the model automatically;
- it does not auto-score answers;
- it does not replace reviewer judgment.
