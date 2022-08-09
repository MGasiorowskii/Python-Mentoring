from typing import Optional


def fizzbuzz(number: int) -> None or str:
    """
    Function return:
    "Fizz" - if number is only divisible by 3
    "Buzz" - if number is only divisible by 5
    "FizzBuzz" - if number is divisible by 3 and 5
    None - otherwise
    """
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
