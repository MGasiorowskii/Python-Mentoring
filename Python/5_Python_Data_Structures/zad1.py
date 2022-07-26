from __future__ import annotations


def common_element(list1: list[int], list2: list[int]) -> bool:

    for element in list1:
        if element in list2:
            return True

    return False


def main():
    a = [2, 3, 4, 5, 6]
    b = [6, 7, 8]

    print(common_element(a, b))


if __name__ == "__main__":
    main()
