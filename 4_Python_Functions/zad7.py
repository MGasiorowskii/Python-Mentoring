import time


def angle_from_time(**kwargs) -> float:
    """
    Return the angle between pointers on the clock
    """
    value_hour = kwargs["hour"]
    value_minute = kwargs["minute"]

    minute_angle = value_minute * 6

    if value_hour >= 12:
        hour_angle = (value_hour - 12) * 30 + (0.5 * value_minute)
    else:
         hour_angle = value_hour * 30 + (0.5 * minute_angle)

    return abs(hour_angle - minute_angle)


def main():

    hour = time.localtime()[3]
    minute = time.localtime()[4]

    print(angle_from_time(hour=hour, minute=minute))


if __name__ == "__main__":
    main()
