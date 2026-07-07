# Payer Contract Checker

Checks synthetic reimbursements against contract rules.

## What it includes

- deterministic sample data
- scoring and ranking logic
- command line report
- unit tests
- continuous validation workflow

## Run

```bash
python3 -m payer_contract_checker.cli --input data/sample_reimbursements.json
```

## Test

```bash
python3 -m unittest discover tests
```
