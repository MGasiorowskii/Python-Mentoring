print("a)")
for column in range(6):
    for line in range(7):
        print("*", end="")
    print()

print("b)")
for column in range(5):
    if (column == 0) or (column == 4):
        print("*" * 5, end="")
    else:
        for line in range(5):
            if (line == 0) or (line == 4):
                print("*", end="")
            else:
                print(" ", end="")
    print()

print("c1)")
spaces = [n for n in range(5, 0, -1)]
for star, space in enumerate(spaces, 1):
    print(" " * space, end="")
    print("*" * (2*star - 1), end="")
    print()

print("c2)")
spaces = [n for n in range(5, 0, -1)]
stars = [n for n in range(1, 6)]
for star, space in zip(stars, spaces):
    print(" " * space, end="")
    print("*" * (2*star - 1), end="")
    print()

