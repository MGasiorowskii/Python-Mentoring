def fizz_buzz(number: int) -> None:
    """
    Function return:
    "Fizz" - if number is divisible by 3
    "Buzz" - if number is divisible by 5
    "FizzBuzz" - if number is divisible by 3 and 5
    number - otherwise
    """
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


def main():
    number: int = int(input("Input any number: "))

    for value in range(number):
        fizz_buzz(value)


if __name__ == "__main__":
    main()
