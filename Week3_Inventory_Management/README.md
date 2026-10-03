# Week 3 – In-Memory Inventory Management Tool

**Student:** Munni Khan  
**Course:** AIM 401 Python Programming for Data Science – International American University  
**Assignment:** Lesson 3 Individual Assignment

A Python script for a distribution centre (the *Kathmandu Valley Distribution Hub*). It
processes a batch of customer orders against an in-memory stock dictionary. For each order it
fully fulfills, partially fulfills, or rejects it (out of stock or unknown item), then prints an end-of-batch
summary report.

## Project structure

```
Week3_Inventory_Management/
├── week3_inventory_management.ipynb # main notebook (Run All)
└── README.md
```

## How to run

Open `week3_inventory_management.ipynb` in VS Code or Jupyter, select the **Munni Khan** kernel and click **Run All**.

No third-party packages are needed. The program uses only Python built-ins.

## How the requirements are met

| Requirement | Implementation |
|---|---|
| Inventory dictionary (≥ 4 items) | `inventory` has 6 products, one of them (USB Hub) starting at 0 |
| Order queue as list of lists/tuples | `order_queue` is a list of 11 `(product, quantity)` tuples |
| Key lookups | `inventory.get(product)`, which returns `None` for unknown products |
| Full fulfillment | `available >= requested`: subtract the full quantity and print SUCCESS |
| Partial fulfillment | `0 < available < requested`: ship the remaining stock, set it to 0 and record the shortfall |
| Out of stock / invalid | `available == 0` or the key is missing: print ALERT and record the shortfall |
| Unfulfilled list | `unfulfilled_items` holds `(product, short_qty)` tuples |
| Summary | final dictionary, count of fully fulfilled orders, list of unsupplied items |

**Constraints respected:** no `def`, no classes, no `import`, and no file reading or writing.
