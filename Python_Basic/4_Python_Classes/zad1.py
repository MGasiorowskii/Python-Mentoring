class Student:
    def __init__(self, year: int, age: int, field_of_study: str) -> None:
        self.year = year
        self.age = age
        self.field_of_study = field_of_study

    def get_info(self) -> list[int, int, str]:
        return [self.year, self.age, self.field_of_study]


def main():
    Mateusz: Student = Student(5, 25, "Electrical Engineering")

    print(Mateusz.get_info())


if __name__ == "__main__":
    main()
