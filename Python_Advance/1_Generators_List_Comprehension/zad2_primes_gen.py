def prime_numbers() -> int:
    """
    Generator of prime numbers
    """
    N = 100
    primes = set([])

    for i in range(2, N + 1):
        primes.update({i})

    for i in range(2, N + 1):
        if i in primes:
            for j in range(2 * i, N + 1, i):
                primes.discard(j)

    for num in primes:
        yield num


def main():
    gen = prime_numbers()
    for num in gen:
        print(num)


if __name__ == "__main__":
    main()
