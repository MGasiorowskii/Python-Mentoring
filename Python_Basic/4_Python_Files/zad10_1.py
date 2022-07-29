
def main():

    max_list = []
    min_list = []
    with open("dane.txt") as binary_file:
        for line in binary_file.readlines():
            max_list.append(max(line.split(" ")))
            min_list.append(min(line.split(" ")))

    with open("results.txt", "a") as file:
                file.write("10.1\n")
                file.write(f"Value of the brightest pixel: {(max(max_list))}")
                file.write(f"Value of the darkest pixel: {(min(min_list))}\n")


if __name__ == "__main__":
    main()
