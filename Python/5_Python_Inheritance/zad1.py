class Shape:
    def __init__(self, length_: float) -> None:
        self.length = length_

    def count_field(self):
        return 0


class Square(Shape):
    def __int__(self, length: float) -> None:
        super().__init__(length)

    def count_field(self) -> float:
        return self.length ** 2


def main():
    p1 = Square(5)
    print(p1.count_field())


if __name__ == "__main__":
    main()
