# Week 4 – Banking Transaction Audit

**Student:** Munni Khan  
**Course:** AIM 401 Python Programming for Data Science – International American University  
**Assignment:** Lesson 4 Individual Assignment

A small audit tool for a bank's daily transactions. It cleans a raw batch of amounts, takes a
service fee off each valid amount, and adds up nested transfer batches with recursion.

## Project structure

```
Week4_Banking_Audit/
├── week4_banking_audit.ipynb # main notebook (Run All)
└── README.md
```

## How to run

Open `week4_banking_audit.ipynb` in VS Code or Jupyter, select the **munnikhan** kernel and click **Run All**.

No third-party packages are needed. The program uses only Python built-ins.

## Functions

| Function | What it does |
|---|---|
| `clean_transactions(amounts, min_threshold=10.0)` | `filter` + `lambda`: keeps only real numbers (not `bool`, not strings) that are positive and at least the threshold |
| `apply_service_fee(amounts, fee_rate=0.02)` | `map` + `lambda`: takes the fee off each amount and rounds to cents |
| `calculate_nested_total(batch)` | recursion: adds every number in a list however deep it is nested, with base cases for a single number and an empty list |

The last cell shows Python's recursion limit (1000) and the `RecursionError` that a very long flat batch causes.
