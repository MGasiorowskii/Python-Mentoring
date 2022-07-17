import time


def angle_from_time(**kwargs) -> float:
    """
    Return the angle between pointers on the clock
    """

    return kwargs


def main():

    hour = time.localtime()[3]
    minute = time.localtime()[4]

    print(angle_from_time(hour=hour, minute=minute))


if __name__ == "__main__":
    main()
