def main():
    with open("example_2.txt", "r+", encoding="utf-8") as file:
        for line in file.readlines():
            new_line = []
            for word in line.split(" "):
                if word not in new_line:
                    file.write(word + " ")


if __name__ == "__main__":
    main()
