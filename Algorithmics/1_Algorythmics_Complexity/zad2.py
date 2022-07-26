from typing import Union


#ktory bedziesz najsyzbszy ?
# jak ograniczyc liczby po ktorych szukamy q?

#x = (q / x - p) ** (1/2)
#x = (q-px) ** (1/3)


def find_x() -> Union[int, str]:
    param = [int(i) for i in input().split(" ")]
    p = param[0]
    q = param[1]

    for value in range(1, q):
        x = q / (value**2 + p)

        if x == value:
            return int(x)

    return "NO"


def main():
    loop = int(input("Input the number o operations: "))
    result = []

    print("Input pairs of numbers: ")
    for i in range(loop):
        result.append(find_x())

    print("Result:")
    [print(x) for x in result]


if __name__ == "__main__":
    main()
