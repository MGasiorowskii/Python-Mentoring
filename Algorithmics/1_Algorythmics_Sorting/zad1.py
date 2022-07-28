import datetime
import random


def measure_time_and_save(array: list) -> None:
    array2 = array.copy()
    array3 = array.copy()
    length = len(array)
    results = []

    for i in range(3):
        t1 = datetime.datetime.now()

        if i == 0:
            bubble_sort(array)
        elif i == 1:
            insertion_sort(array2)
        else:
            quick_sort(array3, 0, len(array3) - 1)

        t2 = datetime.datetime.now()
        results.append(t2 - t1)

    line = f"Times of sorting of arrays of {length} elements:\n- Bubble sorting: {results[0]}\n- Insertion sorting: " \
           f"{results[1]}\n- Quick sorting: {results[2]}\n\n"

    with open("results.txt", "a") as f:
        f.writelines(line)


def bubble_sort(array: list) -> None:
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def insertion_sort(array: list) -> None:
    for i in range(1, len(array)):
        key = array[i]

        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key


def partition(array: list, i: int, j: int) -> int:
    pivot_idx = (i + j) // 2
    pivot = array[pivot_idx]

    while i <= j:
        while pivot > array[i]:
            i += 1

        while pivot < array[j]:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    return i


def quick_sort(array: list, start: int, end: int) -> None:
    edge = partition(array, start, end)

    if start < edge - 1:
        quick_sort(array, start, edge - 1)

    if end > edge:
        quick_sort(array, edge, end)


def main():

    array = [random.randint(0, 100) for _ in range(1_000_000)]
    measure_time_and_save(array)


'''
    array = [random.randint(0, 100) for _ in range(1000)] 
    measure_time_and_save(array)

    array = [random.randint(0, 100) for _ in range(10000)]
    measure_time_and_save(array)

    array = [random.randint(0, 1000) for _ in range(100_000)]
    measure_time_and_save(array)    
'''


if __name__ == "__main__":
    main()
