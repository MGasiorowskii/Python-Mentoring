from __future__ import annotations
from typing import Any


class Vehicles:
    def __init__(self, max_speed_: int, number_: int, depot_: Depot) -> None:
        self.max_speed = max_speed_
        self.number = number_
        self.depot = depot_


class Depot:
    def __init__(self, name_: str, typ_: str):
        self.name = name_
        self.typ = typ_
        self.list_of_vehicles = []

    def __str__(self):
        print(f"{self.name} - {self.typ} type\nList of vehicles in dept:")
        for vehicle in self.list_of_vehicles:
            print(vehicle)
        return ""

    def add_vehicles(self, *args: Any[Tramway, Bus]) -> None:
        for vehicle in args:
            if vehicle.depot.typ == self.typ:
                self.list_of_vehicles.append(vehicle)

    def count_wagons(self) -> Any[int, str]:
        total_wagons = 0
        for tram in self.list_of_vehicles:
            if tram.depot.typ == "Tram":
                total_wagons += tram.wagons_number
            else:
                return "Incorrect data"

        return total_wagons

    def consumed_fuel(self) -> Any[int, str]:
        total_fuel = 0
        for bus in self.list_of_vehicles:
            if bus.depot.typ == "Bus":
                total_fuel += bus.fuel
            else:
                return "Incorrect data"

        return total_fuel


class Tramway(Vehicles):
    def __init__(self, max_speed: int, number: int, depot: Depot, wagons_number_: int) -> None:
        super().__init__(max_speed, number, depot)
        self.wagons_number = wagons_number_

    def __str__(self):
        return f"-max speed: {self.max_speed}\n-number: {self.number}\n-depot: {self.depot.name}\n" \
               f"-wagons number: {self.wagons_number}\n"


class Bus(Vehicles):
    def __init__(self, max_speed: int, number: int, depot: Depot, fuel_: int) -> None:
        super().__init__(max_speed, number, depot)
        self.fuel = fuel_

    def __str__(self):
        return f"-max speed: {self.max_speed}\n-number: {self.number}\n-depot: {self.depot.name}\n" \
               f"-consumed_fuel: {self.fuel}\n"


def main():

    bus_depot = Depot("Podgorze", "Bus")
    tram_depot = Depot("Krowodrza", "Tram")

    bus1 = Bus(120, 103, bus_depot, 50)
    bus2 = Bus(100, 201, bus_depot, 80)
    tramway1 = Tramway(60, 10, tram_depot, 1)
    tramway2 = Tramway(70, 14, tram_depot, 2)
    tramway3 = Tramway(80, 50, tram_depot, 3)

    bus_depot.add_vehicles(bus1, bus2, tramway1, tramway2, tramway3)
    tram_depot.add_vehicles(bus1, bus2, tramway1, tramway2, tramway3)

    print(bus_depot)
    print(tram_depot)

    print(bus_depot.consumed_fuel())
    print(tram_depot.count_wagons())


if __name__ == "__main__":
    main()
