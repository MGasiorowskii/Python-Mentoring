class Vehicle:
    """
    Class represented the vehicle xyz

    """
    def __init__(self, max_speed_: int, cars_millage_: float) -> None:
        self.max_speed = max_speed_
        self.cars_millage = cars_millage_

    def increase_cars_millage(self, distance: float) -> None:
        """Function to increase car mileage by passed value"""
        self.cars_millage += distance

    def get_cars_millage(self) -> float:
        """Simple method to return the object cars_mileage"""
        return self.cars_millage


def main():
    audi = Vehicle(260, 1650)

    audi.increase_cars_millage(23.5)
    print(audi.get_cars_millage())


if __name__ == "__main__":
    main()
