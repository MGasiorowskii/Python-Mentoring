import random


def crash():
    numbers = [random.Random(100) for x in range(100)]
    return crash()


def main():
    crash()


if __name__ == "__main__":
    main()
