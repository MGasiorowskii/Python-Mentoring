from functionality.operations import primary_numbers


def test_should_return_false_for_zero_value():
    num = 0

    assert primary_numbers(num) == False


def test_should_return_false_for_negative_values():
    num1 = -3
    num2 = -1

    assert primary_numbers(num1) == False
    assert primary_numbers(num2) == False


def test_should_return_false_for_one_value():
    num = 1

    assert primary_numbers(num) == False


def test_should_return_true_for_postive_primary_values():
    num1 = 2
    num2 = 5

    assert primary_numbers(num1) == True
    assert primary_numbers(num2) == True


def test_should_return_false_for_postive_not_primary_values():
    num1 = 4
    num2 = 8

    assert primary_numbers(num1) == False
    assert primary_numbers(num2) == False


"""
def test_should_return_false_for_string_values():


def test_should_return_false_for_float_values():

"""