def main():
    with open("example_2.txt", "r", encoding="utf-8") as file_r:
        with open("new_example.txt", "w", encoding="utf-8") as file_w:
            for line in file_r.readlines():
                new_line = []
                for word in line.split(" "):
                    if word + " " not in new_line:
                        new_line.append(word + " ")

                file_w.writelines(new_line)


if __name__ == "__main__":
    main()
