def rec_print(n: int) -> None:
    print(n, end=" ")
    if n > 0:
        return rec_print(n-1)


def main():
    n = 21
    rec_print(n)


if __name__ == "__main__":
    main()
