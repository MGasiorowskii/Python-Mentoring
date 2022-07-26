def main():
    with open("example.txt", encoding="utf-8") as file:
        all_lines = file.readlines()
        for index, line in enumerate(all_lines, 1):
            if index % 2 == 0:
                print(line)


if __name__ == "__main__":
    main()
