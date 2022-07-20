class Rectangle:
    def __init__(self, width_: float, length_: float):
        self.width = width_
        self.length = length_

    def calculate_area(self) -> float:
        return self.width * self.length

    def calculate_circuit(self) -> float:
        return 2 * (self.width + self.length)


def main():
    figure1 = Rectangle(12.3, 3.5)

    print(f"Area of rectangle: {round(figure1.calculate_area(), 2)}")
    print(f"Circuit of rectangle: {figure1.calculate_circuit()}")


if __name__ == "__main__":
    main()