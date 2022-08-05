import time
from dataclasses import dataclass, asdict, astuple


def timethis(func):
    def inner(t1: float):
        t2 = time.time()
        func(t2 - t1)
    return inner


@timethis
def decorating_time(tim: float):
    print(f"Decorating time: {tim}")


decorating_time(time.time())

class Car:
    def __init__(self, name):
        self.name = name


    @classmethod
    def create_from_url(cls, url):
        name = url[:5]
        return cls(name=name)

    @staticmethod
    def x():
        print("test")


class Car_2(Car):
    pass


Car_2.x()
car = Car("Ford")
car_1 = Car.create_from_url("qweqweqweqw")


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name + "wow"

    @name.setter
    def name(self, name):
        self.__name = name

    @name.getter
    def name(self):
        return self.__name

    def __ge__(self, other):
        pass


person = Person("Robert")
print(person.name)

@dataclass(frozen=True)
class Person_d:
    first_name: str = "Ahmed"
    last_name: str = "Basbes"
    def __post_init__(self):
        full_name = self.first_name + self.last_name

robert = Person_d()
print(robert)
print(asdict(robert))
print(astuple(robert))
robert.first_name = "last_name"