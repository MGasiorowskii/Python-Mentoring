class Student:
    def __init__(self, year_: int, age_: int, field_of_study_: str):
        self.year = year_
        self.age = age_
        self.field_of_study = field_of_study_

    def get_info(self) -> list[int, int, str]:
        return [self.year, self.age, self.field_of_study]


def main():
    Mateusz = Student(5, 25, "Electrical Engineering")

    print(Mateusz.get_info())


if __name__ == "__main__":
    main()
