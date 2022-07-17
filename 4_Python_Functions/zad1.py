def max_element_and_index(numbers: list[int]) -> [int, int]:
    """
    Return the max value and index of this number
    """
    for index, number in enumerate(numbers):
        if number == max(numbers):
            return [number, index]


def main():
    nums = [4, 6, 8, 24, 12, 2]

    print(max_element_and_index(nums))


if __name__ == "__main__":
    main()
