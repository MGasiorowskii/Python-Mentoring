from __future__ import annotations
from typing import Optional, Union
import time


class Tank:
    def __init__(self, name_: str, max_volume_: int, actual_level_: Optional[int] = 0) -> None:
        self.name = name_
        self.max_volume = max_volume_
        self.actual_level = actual_level_
        self.logs = []
        self.struct = {"Date": "",
                       "Time": "",
                       "Operation": "",
                       "Tank Name": "",
                       "Volume": "",
                       "Result": False}

    def __str__(self):
        return f"Name: {self.name}\nMax Volume: {self.max_volume}\nActual Level: {self.actual_level}\nLogs: {self.logs}\n"

    def pour_water(self, volume: int) -> bool:

        self.struct["Date"] = time.strftime("%m/%d/%Y", time.localtime())
        self.struct["Time"] = time.strftime("%H:%M:%S", time.localtime())
        self.struct["Operation"] = "pour_water"
        self.struct["Tank Name"] = self.name
        self.struct["Volume"] = volume

        if self.actual_level + volume > self.max_volume:
            self.struct["Result"] = False
            self.logs.append(self.struct)
            return False
        else:
            self.struct["Result"] = True
            self.logs.append(self.struct)
            return True

    def pour_out_water(self, volume: int) -> bool:

        self.struct["Date"] = time.strftime("%m/%d/%Y", time.localtime())
        self.struct["Time"] = time.strftime("%H:%M:%S", time.localtime())
        self.struct["Operation"] = "pour_out_water"
        self.struct["Tank Name"] = self.name
        self.struct["Volume"] = volume

        if self.actual_level - volume < 0:
            self.struct["Result"] = False
            self.logs.append(self.struct)
            return False
        else:
            self.struct["Result"] = True
            self.logs.append(self.struct)
            return True

    def transfer_water(self, tank: Tank, volume: int) -> Union[None, bool]:

        if self.pour_water(volume) and tank.pour_out_water(volume):
            self.struct["Date"] = time.strftime("%m/%d/%Y", time.localtime())
            self.struct["Time"] = time.strftime("%H:%M:%S", time.localtime())
            self.struct["Operation"] = "transfer_water"
            self.struct["Tank Name"] = self.name
            self.struct["Volume"] = volume
            self.actual_level += volume
            tank.actual_level -= volume
            self.struct["Result"] = True
            self.logs.append(self.struct)
            return
        else:
            self.struct["Date"] = time.strftime("%m/%d/%Y", time.localtime())
            self.struct["Time"] = time.strftime("%H:%M:%S", time.localtime())
            self.struct["Operation"] = "transfer_water"
            self.struct["Tank Name"] = self.name
            self.struct["Volume"] = volume
            self.struct["Result"] = False
            self.logs.append(self.struct)
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


def main():
    list_of_Tanks = []
    p1 = Tank("Tank 1", 2500)
    p2 = Tank("Tank 2", 1000, 999)
    p3 = Tank("Tank 1", 2000, 500)
    p4 = Tank("Tank 2", 3000, 500)
    print(p1)
    print(p2)
    p1.transfer_water(p2, 2000)
    print(p1)
    print(p2)
    print(most_water(p1, p3, p4))
    print(most_filled(p1, p2, p3, p4))


if __name__ == "__main__":
    main()
