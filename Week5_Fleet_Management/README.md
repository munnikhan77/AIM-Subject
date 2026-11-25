# Week 5 – LogiTrans Logistics Fleet Management Prototype

**Student:** Munni Khan  
**Course:** AIM 401 Python Programming for Data Science – International American University  
**Assignment:** Lesson 5 Individual Assignment

An object-oriented prototype that models a rental fleet of passenger cars and cargo trucks
and prints a billing manifest for any mix of vehicles. It uses all four pillars of OOP.

## Project structure

```
week5-fleet-management/
├── week5_fleet_management.ipynb # main notebook (Run All)
├── fleet_management.py          # same program as a standalone script
├── screenshots/                 # code + output screenshots used in the report
└── README.md
```

## How to run

Open `week5_fleet_management.ipynb` in VS Code or Jupyter, select the **munnikhan** kernel and click **Run All**,
or run `python fleet_management.py`. Only the standard-library `abc` module is used.

## How the requirements are met

| Requirement | Implementation |
|---|---|
| Task 1 – Abstraction | `Vehicle(ABC)` with `vehicle_id`, `model` and the abstract `calculate_rental_cost(days)`; `Vehicle(...)` raises `TypeError` |
| Task 2 – Encapsulation | private `__daily_rate`, `get_daily_rate()` / `set_daily_rate()` (also the `daily_rate` property); the setter raises `ValueError` for values ≤ 0.0 or non-numbers |
| Task 3 – Inheritance | `PassengerCar` (`num_seats`) and `CargoTruck` (`cargo_capacity_tons`) both call `super().__init__(...)` |
| Task 4 – Overriding | car: `(daily_rate × days) + (15.0 × num_seats)`; truck: `(daily_rate × days) + (50.0 × cargo_capacity_tons)` |
| Task 4 – Operator overloading | `__str__()` in both subclasses, `__lt__()` in `Vehicle` so `sorted(fleet)` orders by daily rate |
| Task 4 – Polymorphic processing | `generate_fleet_manifest(fleet_list, days)` calls `calculate_rental_cost()` and `str()` with no `isinstance()` / `type()` |

## Sample result

A 7-day rental of the six-vehicle demo fleet totals **$8,202.50**, and every bill matches a hand calculation (self-check cell). The notebook also includes a cost-breakdown chart and a bonus `ElectricVan` class that shows a new vehicle type needs no change to `generate_fleet_manifest()`.
