def example1():
    for _ in range(3):
        try:
            x = int(input("enter a number: "))
            y = int(input("enter another number: "))
            print(x, '/', y, '=', x / y)
        except ValueError:
            print(f"x and y have to be numbers")
        except ZeroDivisionError:
            print(f"Dont divide by 0")


def example2(L):
    print("\n\nExample 2")

    try:

        sumofpairs = []
        for i in range(len(L)):
            sumofpairs.append(L[i] + L[i + 1])

            print("sumOfPairs = ", sumofpairs)

    except IndexError:
        print("Invalid index of list")
    except TypeError:
        print(f"All elements of list have to be numbers")


def printUpperFile(fileName):
    try:
        file = open(fileName, "r")

        for line in file:
            print(line.upper())
        file.close()
    except PermissionError:
        pass
    except FileNotFoundError:
        print("Incorrect path to file")


def main():
    example1()
    L = [10, 3, 5, 6, 9, 3]
    example2(L)
    example2([10, 3, 5, 6, "NA", 3])
    try:
        example3([10, 3, 5, 6])
    except NameError:
        print("Incorrect name of function")

    printUpperFile("doesNotExistYest.txt")
    printUpperFile("C:/Dessssktop/misspelled.txt")


if __name__ == "__main__":
    main()
