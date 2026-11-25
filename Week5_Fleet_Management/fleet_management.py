"""Lesson 5 - LogiTrans Logistics Fleet Management Prototype
Author: Munni Khan

Shows the four pillars of OOP:
  1. Abstraction    - Vehicle is an abstract base class (abc module).
  2. Encapsulation  - the daily rate is stored in a private __daily_rate attribute
                      and can only be changed through a validating setter.
  3. Inheritance    - PassengerCar and CargoTruck extend Vehicle with super().__init__().
  4. Polymorphism   - each subclass overrides calculate_rental_cost() and __str__(),
                      Vehicle overloads __lt__() for sorting, and
                      generate_fleet_manifest() bills every vehicle the same way.
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------------------------
# Task 1 + Task 2: abstract base class with an encapsulated daily rate
# ---------------------------------------------------------------------------
class Vehicle(ABC):
    """Blueprint for every vehicle in the fleet. It cannot be created directly."""

    def __init__(self, vehicle_id, model, daily_rate):
        self.vehicle_id = vehicle_id
        self.model = model
        self.set_daily_rate(daily_rate)          # goes through the validation below

    # ----- encapsulation: private rate with a getter and a validating setter -----
    def get_daily_rate(self):
        return self.__daily_rate

    def set_daily_rate(self, value):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"Daily rate must be a number, got {value!r}.")
        if value <= 0.0:
            raise ValueError(f"Daily rate must be greater than 0.0, got {value}.")
        self.__daily_rate = float(value)

    # the same getter/setter exposed as a property, so v.daily_rate also works
    daily_rate = property(get_daily_rate, set_daily_rate)

    # ----- abstraction: every subclass must supply its own billing rule -----
    @abstractmethod
    def calculate_rental_cost(self, days):
        """Return the total rental cost for the given number of days."""

    # shared helper, so both subclasses reject bad day counts the same way
    @staticmethod
    def _check_days(days):
        if isinstance(days, bool) or not isinstance(days, int) or days <= 0:
            raise ValueError(f"Rental days must be a positive whole number, got {days!r}.")

    # ----- operator overloading: v1 < v2 compares daily rates (used by sorted()) -----
    def __lt__(self, other):
        if not isinstance(other, Vehicle):
            return NotImplemented
        return self.get_daily_rate() < other.get_daily_rate()

    # developer-friendly representation, handy when debugging lists of vehicles
    def __repr__(self):
        return f"{self.__class__.__name__}({self.vehicle_id!r}, {self.model!r}, {self.daily_rate})"


# ---------------------------------------------------------------------------
# Task 3 + Task 4: child classes with overridden billing and __str__
# ---------------------------------------------------------------------------
class PassengerCar(Vehicle):
    SEAT_FEE = 15.0                               # flat fee per seat

    def __init__(self, vehicle_id, model, daily_rate, num_seats):
        super().__init__(vehicle_id, model, daily_rate)
        if int(num_seats) <= 0:
            raise ValueError("A passenger car needs at least one seat.")
        self.num_seats = int(num_seats)

    def calculate_rental_cost(self, days):
        self._check_days(days)
        return (self.daily_rate * days) + (self.SEAT_FEE * self.num_seats)

    def __str__(self):
        return (f"[Car]   {self.vehicle_id:<7} {self.model:<20} "
                f"${self.daily_rate:>7.2f}/day  {self.num_seats} seats")


class CargoTruck(Vehicle):
    TON_FEE = 50.0                                # flat fee per ton of capacity

    def __init__(self, vehicle_id, model, daily_rate, cargo_capacity_tons):
        super().__init__(vehicle_id, model, daily_rate)
        if float(cargo_capacity_tons) <= 0:
            raise ValueError("Cargo capacity must be greater than 0 tons.")
        self.cargo_capacity_tons = float(cargo_capacity_tons)

    def calculate_rental_cost(self, days):
        self._check_days(days)
        return (self.daily_rate * days) + (self.TON_FEE * self.cargo_capacity_tons)

    def __str__(self):
        return (f"[Truck] {self.vehicle_id:<7} {self.model:<20} "
                f"${self.daily_rate:>7.2f}/day  {self.cargo_capacity_tons:.1f} tons")


# ---------------------------------------------------------------------------
# Task 4: polymorphic processing - no isinstance() or type() in here
# ---------------------------------------------------------------------------
def generate_fleet_manifest(fleet_list, days):
    """Print a billing manifest for any mix of vehicles and return the grand total."""
    line = "=" * 78
    print(line)
    print(f"LOGITRANS LOGISTICS - FLEET RENTAL MANIFEST ({days} day rental)")
    print(line)
    grand_total = 0.0
    for vehicle in fleet_list:
        cost = vehicle.calculate_rental_cost(days)   # each object runs its own formula
        grand_total += cost
        print(f"{str(vehicle):<64} ${cost:>10,.2f}")
    print("-" * 78)
    print(f"{'Vehicles dispatched: ' + str(len(fleet_list)):<64} ${grand_total:>10,.2f}")
    print(line)
    return grand_total


if __name__ == "__main__":
    fleet = [
        PassengerCar("PC-101", "Toyota Corolla", 45.00, 5),
        CargoTruck("CT-201", "Isuzu NPR", 150.00, 3.5),
        PassengerCar("PC-102", "Honda CR-V", 62.50, 5),
        CargoTruck("CT-202", "Volvo FH16", 320.00, 25.0),
        PassengerCar("PC-103", "Toyota Sienna", 85.00, 8),
        CargoTruck("CT-203", "Hino 500", 210.00, 8.0),
    ]

    # Abstraction: the base class cannot be instantiated
    try:
        Vehicle("X-000", "Generic", 10.0)
    except TypeError as err:
        print("Abstraction check  :", err)

    # Encapsulation: validated setter and hidden attribute
    corolla = fleet[0]
    print("Corolla rate       :", corolla.get_daily_rate())
    corolla.set_daily_rate(48.00)
    print("After raise to 48  :", corolla.daily_rate)
    for bad in (0, -25.0, "cheap"):
        try:
            corolla.set_daily_rate(bad)
        except ValueError as err:
            print("Rejected           :", err)
    try:
        print(corolla.__daily_rate)
    except AttributeError as err:
        print("Direct access      :", err)
    corolla.set_daily_rate(45.00)                # back to the normal rate for billing

    # Operator overloading: sort by daily rate using __lt__
    print("\nFleet sorted by daily rate (cheapest first):")
    for v in sorted(fleet):
        print("  ", v)

    # Polymorphic processing
    print()
    generate_fleet_manifest(fleet, 7)
