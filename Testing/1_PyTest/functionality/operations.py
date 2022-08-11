from typing import Union


def primary_numbers(num: int) -> Union[bool, str]:
    if isinstance(num, int):
        dividers = []
        if num > 0:

            for divider in range(1, num + 1):
                if num % divider == 0:
                    dividers.append(divider)

            if len(dividers) == 2:
                return True

        return False
    else:
        return "Invalid data"
