from functionality.FizzBuzz import fizzbuzz


def test_should_return_fizz_for_positive_numbers_divisible_only_by_3():
    nums = [3, 6, 9]
    expected = "Fizz"

    for num in nums:
        assert fizzbuzz(num) == expected


def test_should_return_buzz_for_negative_numbers_divisible_only_by_3():
    nums = [-3, -6, -9]
    expected = "Fizz"

    for num in nums:
        assert fizzbuzz(num) == expected


def test_should_return_fizz_for_positive_numbers_divisible_only_by_5():
    nums = [5, 10, 20]
    expected = "Buzz"

    for num in nums:
        assert fizzbuzz(num) == expected


def test_should_return_fizz_for_negative_numbers_divisible_only_by_5():
    nums = [-5, -10, -20]
    expected = "Buzz"

    for num in nums:
        assert fizzbuzz(num) == expected


def test_should_return_fizzbuzz_for_zero_value():
    num = 0
    expected = "FizzBuzz"

    assert fizzbuzz(num) == expected


def test_should_return_fizzbuzz_for_positive_numbers_divisible_by_3_and_5():
    nums = [15, 30]
    expected = "FizzBuzz"

    for num in nums:
        assert fizzbuzz(num) == expected


def test_should_return_fizzbuzz_for_negative_numbers_divisible_by_3_and_5():
    nums = [-15, -30]
    expected = "FizzBuzz"

    for num in nums:
        assert fizzbuzz(num) == expected


def test_should_return_none_for_positive_numbers_not_divisible_by_3_and_5():
    nums = [1, 2, 4, 7]
    expected = None

    for num in nums:
        assert fizzbuzz(num) == expected


def test_should_return_none_for_negative_numbers_not_divisible_by_3_and_5():
    nums = [-1, -2, -4, -7]
    expected = None

    for num in nums:
        assert fizzbuzz(num) == expected
