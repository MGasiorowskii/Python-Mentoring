def kwargs_to_list(**kwargs) -> list[int]:
    """
    Return sorted list
    """
    list_of_numbers = []
    key_even = "even_number"
    key_odd = "odd_numbers"
    for value_even, value_odd in zip(kwargs[key_even], kwargs[key_odd]):
        list_of_numbers.extend([value_even, value_odd])

    return list_of_numbers


def main():

    print(kwargs_to_list(even_number=[0, 2, 4, 6, 8], odd_numbers=[1, 3, 5, 7, 9]))


if __name__ == "__main__":
    main()
