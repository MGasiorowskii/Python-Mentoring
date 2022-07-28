from __future__ import annotations
from typing import Optional, Union
import time


class Tank:
    def __init__(self, name_: str, max_volume_: int, actual_level_: Optional[int] = 0) -> None:
        self.name = name_
        self.max_volume = max_volume_
        self.actual_level = actual_level_
        self.logs: list[dict] = []

    def __str__(self) -> str:
        return f"Name: {self.name}\nMax Volume: {self.max_volume}\nActual Level: {self.actual_level}\nLogs: {self.logs}\n"

    def logging(self, operation: str, name: str, volume: int, result: bool) -> None:
        struct = {"Date": "",
                  "Time": "",
                  "Operation": "",
                  "Tank Name": "",
                  "Volume": 0,
                  "Result": False}
        struct["Date"] = time.strftime("%m/%d/%Y", time.localtime())
        struct["Time"] = time.strftime("%H:%M:%S", time.localtime())
        struct["Operation"] = operation
        struct["Tank Name"] = name
        struct["Volume"] = volume
        struct["Result"] = result
        self.logs.append(struct)

    def pour_water(self, volume: int) -> bool:
        if self.actual_level + volume > self.max_volume:
            self.logging("pour_water", self.name, volume, False)
            return False

        self.logging("pour_water", self.name, volume, True)
        return True

    def pour_out_water(self, volume: int) -> bool:

        if self.actual_level - volume < 0:
            self.logging("pour_out_water", self.name, volume, False)
            return False
        else:
            self.logging("pour_out_water", self.name, volume, True)
            return True

    def transfer_water(self, tank: Tank, volume: int) -> Union[None, bool]:

        if self.pour_water(volume) and tank.pour_out_water(volume):
            self.actual_level += volume
            tank.actual_level -= volume
            self.logging("transfer_water", self.name, volume, True)
            return
        else:
            self.logging("transfer_water", self.name, volume, False)
            print("the operation cannot be performed\n")
            return False


def most_water(*args: Tank) -> list[str, ...]:
    max_value = 0
    name = []
    for tank in args:
        if tank.actual_level > max_value:
            max_value = tank.actual_level
            name.clear()
            name.append(tank.name)
        elif tank.actual_level == max_value:
            name.append(tank.name)

    return name


def most_filled(*args: Tank) -> list[str, ...]:
    # x.sort(key=lambda: tank.actual_level/ tank.max_volume)
    # x[-1]
    max_value = 0
    name = []
    for tank in args:
        fill = (tank.actual_level / tank.max_volume)

        if fill > max_value:
            max_value = tank.actual_level
            name.clear()
            name.append(tank.name)
        elif fill == max_value:
            name.append(tank.name)

    return name


def empty_tanks(*args: Tank) -> list[str, ...]:
    name = []
    for tank in args:
        if tank.actual_level == 0:
            name.append(tank.name)

    return name


def most_false(*args: Tank) -> list[str, ...]:
    max_value = 0
    name = []
    for tank in args:
        number_of_false = 0
        for log in tank.logs:
            if not log["Result"]:
                number_of_false += 1
        if number_of_false > max_value:
            max_value = number_of_false
            name.clear()
            name.append(tank.name)
        elif number_of_false == max_value:
            name.append(tank.name)

    return name


def most_operation(*args: Union[Tank, str]) -> list[str, ...]:
    max_value = 0
    name = []
    for tank in args[:-1]:
        number_of_operation = 0
        for log in tank.logs:
            if log["Operation"] == args[-1]:
                number_of_operation += 1
        if number_of_operation > max_value:
            max_value = number_of_operation
            name.clear()
            name.append(tank.name)
        elif number_of_operation == max_value:
            name.append(tank.name)

    return name


def check_state(initial_volume: int, tank: Tank) -> bool:

    for log in tank.logs:
        if log["Operation"] == "pour_water":
            initial_volume += log["Volume"]
        elif log["Operation"] == "pour_out_water":
            initial_volume -= log["Volume"]

    if initial_volume == tank.actual_level:
        return True
    return False


def main():

    p1 = Tank("Tank 1", 2500)
    p2 = Tank("Tank 2", 1000, 999)
    p3 = Tank("Tank 3", 2000, 500)
    p4 = Tank("Tank 4", 3000, 500)
    print(p1)
    print(p2)
    p1.transfer_water(p2, 500)
    print(p1)
    print(p2)
    print(most_water(p1, p3, p4))
    print(most_filled(p1, p2, p3, p4))
    print(most_false(p1, p2, p3, p4))
    print(most_operation(p1, p2, p3, p4, "pour_out_water"))
    print(check_state(0, p1))


if __name__ == "__main__":
    main()
