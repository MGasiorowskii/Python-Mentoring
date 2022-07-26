def multiplication(*args: int) -> int:
    """
    Return the max value from any number of arguments
    """
    score = 1
    for value in args:
        score *= value

    return score


def main():
    nums = [5, 7, 8]   #Jak przekazywać tablice do *args ?

    print(*nums)
    print(multiplication(*nums, 10))


if __name__ == "__main__":
    main()
