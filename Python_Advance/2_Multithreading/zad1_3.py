import random
import time
from multiprocessing import Pool
from threading import Thread


def random_int() -> list[int]:
    return [random.randint(0, 1000) for _ in range(1000)]


def bubble_sort(arrays) -> None:
    for array in arrays:
        for i in range(len(array)):
            for j in range(len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]


def main():
    array1 = random_int()
    array2 = random_int()
    array3 = random_int()
    array4 = random_int()
    array5 = random_int()
    array6 = random_int()
    array7 = random_int()
    array8 = random_int()
    array9 = random_int()
    array10 = random_int()

    array1_p = array1.copy()
    array2_p = array2.copy()
    array3_p = array3.copy()
    array4_p = array4.copy()
    array5_p = array5.copy()
    array6_p = array6.copy()
    array7_p = array7.copy()
    array8_p = array8.copy()
    array9_p = array9.copy()
    array10_p = array10.copy()

    t1 = Thread(target=bubble_sort, args=[[array1, array2, array3, array4, array5]])
    t2 = Thread(target=bubble_sort, args=[[array6, array7, array8, array9, array10]])

    start = time.time()
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end = time.time()
    print(f"Time of multithreading in seconds: {end - start}")

    pool = Pool(processes=2)
    start = time.time()
    p1 = pool.apply_async(bubble_sort, [array1_p, array2_p, array3_p, array4_p, array5_p])
    p2 = pool.apply_async(bubble_sort, [array6_p, array7_p, array8_p, array9_p, array10_p])

    pool.close()
    pool.join()
    end = time.time()
    print(f"Time of multitprocessing in seconds: {end - start}")


if __name__ == "__main__":
    main()
