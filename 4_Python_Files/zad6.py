def main():
    with open("test.txt") as file:
        lines = file.readlines()
        print(lines[3])


if __name__ == "__main__":
    main()