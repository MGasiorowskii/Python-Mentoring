def fibonacci_numbers(nums):
    a = 1
    b = 2
    yield 0
    yield a
    yield a
    yield b
    for _ in range(nums):
        a, b = b, a+b
        yield b


def main():
    for num in fibonacci_numbers(15):
        print(num, end=" ")


if __name__ == "__main__":
    main()
