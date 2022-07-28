from typing import Union
from datetime import datetime


class Case:
    TIME_FORMAT = "%Y-%m-%dT%H:%M:%S+00:00"
    def retrieve_seconds(self, case_number) -> Union[int, str]:
        if case_number['created_task'] is None or case_number['end_task'] is None:
            return "Task still continues"

        created_task = datetime.strptime(case_number['created_task'], Case.TIME_FORMAT)
        end_task = datetime.strptime(case_number['end_task'], Case.TIME_FORMAT)

        return int(end_task.timestamp() - created_task.timestamp())


def main():
    first_case = {
        "name": "first_case",
        "created_task": "2021-10-26T19:48:12+00:00",
        "end_task": None
    }
    second_case = {
        "name": "second_case",
        "created_task": "2021-09-26T19:48:12+00:00",
        "end_task": "2021-10-26T19:48:12+00:00"
    }

    p1 = Case()
    print(p1.retrieve_seconds(second_case))
    print(p1.retrieve_seconds(first_case))


if __name__ == "__main__":
    main()
