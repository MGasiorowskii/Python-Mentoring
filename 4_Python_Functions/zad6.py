import random

# Czy da się określic maksymlana liczbe argumentów listy ?
def filter_list(list_of_numbers: list[int]) -> list[int]:
    """
    Return filtered list that contains only two-digit numbers from 10-element list
    """
    sorted_list = []
    for number in list_of_numbers:
        if 10 <= number <= 99:
            sorted_list.append(number)

    return sorted_list


def main():

    list_to_sort = []
    for value in range(10):
        list_to_sort.append(random.randint(1, 115))

    print(list_to_sort)
    print(filter_list(list_to_sort))


if __name__ == "__main__":
    main()
