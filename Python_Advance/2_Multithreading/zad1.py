import random
import time
from multiprocessing import Pool
from threading import Thread


def random_int() -> list[int]:
    return [random.randint(0, 1000) for _ in range(10000)]


def bubble_sort_one(array: list) -> None:
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

    t1 = Thread(target=bubble_sort_one, args=[array1])
    t2 = Thread(target=bubble_sort_one, args=[array2])
    t3 = Thread(target=bubble_sort_one, args=[array3])
    t4 = Thread(target=bubble_sort_one, args=[array4])
    t5 = Thread(target=bubble_sort_one, args=[array5])
    t6 = Thread(target=bubble_sort_one, args=[array6])
    t7 = Thread(target=bubble_sort_one, args=[array7])
    t8 = Thread(target=bubble_sort_one, args=[array8])
    t9 = Thread(target=bubble_sort_one, args=[array9])
    t10 = Thread(target=bubble_sort_one, args=[array10])

    start = time.time()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    end = time.time()
    print(f"Time of multithreading in seconds: {end - start}")

    pool = Pool(processes=10)
    start = time.time()
    p1 = pool.apply_async(bubble_sort_one, [array1_p])
    p2 = pool.apply_async(bubble_sort_one, [array2_p])
    p3 = pool.apply_async(bubble_sort_one, [array3_p])
    p4 = pool.apply_async(bubble_sort_one, [array4_p])
    p5 = pool.apply_async(bubble_sort_one, [array5_p])
    p6 = pool.apply_async(bubble_sort_one, [array6_p])
    p7 = pool.apply_async(bubble_sort_one, [array7_p])
    p8 = pool.apply_async(bubble_sort_one, [array8_p])
    p9 = pool.apply_async(bubble_sort_one, [array9_p])
    p10 = pool.apply_async(bubble_sort_one, [array10_p])
    pool.close()
    pool.join()
    end = time.time()
    print(f"Time of multitprocessing in seconds: {end - start}")


if __name__ == "__main__":
    main()
