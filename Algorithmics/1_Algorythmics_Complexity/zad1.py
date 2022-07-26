import random


def binary_search(numbers: list[int], value: int) -> bool:
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] < 20:
            left = mid + 1
        elif numbers[mid] > 20:
            right = mid - 1
        else:
            break

    if len(numbers) - mid - 1 >= 10:
        return True
    else:
        return False


def main():
    numbers = []
    for number in range(30):
        numbers.append(random.randint(0, 30))

    numbers.sort()
    print(numbers)
    print(binary_search(numbers, 20))


if __name__ == "__main__":
    main()
