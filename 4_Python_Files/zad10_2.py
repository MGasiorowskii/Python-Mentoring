
def main():

    numbers_line_to_remove = 0
    with open("dane.txt") as binary_file:
        for number, line in enumerate(binary_file.readlines(), 1):
            split_line = line.split()
            for i in range(160):
                if split_line[i] != split_line[-(i+1)]:
                    numbers_line_to_remove += 1
                    # print(f"Line number {number} should be removed")
                    break

    with open("results.txt", "a") as file:
        file.write("10.2\n")
        file.write(f"The smallest number of line to be removed: {numbers_line_to_remove}\n")


if __name__ == "__main__":
    main()
