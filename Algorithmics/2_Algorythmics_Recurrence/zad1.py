import random


def print_list(tab: list[int]) -> None:
    if len(tab) > 1:

        print(tab.pop(0), end=" ")
        return print_list(tab)
    else:
        print(tab[0])
        return


def main():
    tab = [random.randint(1, 50) for x in range(15)]
    print(tab)
    print_list(tab)


if __name__ == "__main__":
    main()
