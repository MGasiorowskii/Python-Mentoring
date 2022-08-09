import random
import pytest
from functionality.quicksort import *


@pytest.fixture
def get_list_of_rand_nums() -> list[int]:
    return [random.randint(1, 100) for i in range(20)]


def test_if_list_is_sorted_by_function(get_list_of_rand_nums):

    result = get_list_of_rand_nums
    expected = get_list_of_rand_nums.copy()
    expected.sort()
    quick_sort(result, 0, len(result) - 1)

    assert result == expected


def test_if_list_is_sorted_by_comparing(get_list_of_rand_nums):
    is_valid = True

    result = get_list_of_rand_nums
    quick_sort(result, 0, len(result) - 1)

    for i in range(len(result) - 1):
        if result[i] > result[i+1]:
            is_valid = False

    assert is_valid
