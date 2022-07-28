def calc_NWD(a: int, b: int) -> int:
    if b > a:
        a, b = b, a

    if b == 0:
        return a

    return calc_NWD(b, a % b)


def calc_NWW(a: int, b: int) -> int:

    return int((a * b) / calc_NWD(a, b))


def main():

    a = 12
    b = 8
    print(calc_NWD(a, b))
    print(calc_NWW(a, b))


if __name__ == "__main__":
    main()
