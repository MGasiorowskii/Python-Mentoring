
def main():

    new_list = []
    with open("dane.txt") as binary_file:
        for line in binary_file.readlines():
            split_line = [int(x) for x in line.split()]
            new_list.append(split_line)

    max_vertical_line = 1
    for column in range(320):
        vertical_line = 1
        for line in range(199):

            if new_list[line][column] == new_list[line+1][column]:
                vertical_line += 1

        if vertical_line > max_vertical_line:
            max_vertical_line = vertical_line

    with open("results.txt", "a") as file:
                file.write("10.4\n")
                file.write(f"The longest vertical line: {max_vertical_line}\n")


if __name__ == "__main__":
    main()
