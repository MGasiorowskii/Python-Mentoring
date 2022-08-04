import random


def random_numbers():
    """
    Generator of random numbers
    """

    while True:
        num = random.randint(0, 1000)
        yield num


def main():
    gen = random_numbers()
    for num in gen:
        if num > 800:
            gen.throw(ValueError("too big number!"))
        else:
            print(num)


if __name__ == "__main__":
    main()
