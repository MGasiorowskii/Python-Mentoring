
def main():

    new_list = []
    contrasting_pixels = 0
    with open("dane.txt") as binary_file:
        for line in binary_file.readlines():
            split_line = [int(x) for x in line.split()]
            new_list.append(split_line)

    for line in range(200):
        for column in range(320):
            value = new_list[line][column]
            if line == 0 and column == 0:
                if abs(new_list[line+1][column] - value) > 128:
                    contrasting_pixels += 1
                elif abs(new_list[line+1][column] - value) > 128:
                    contrasting_pixels += 1

            elif line == 0 and column == 319:
                if abs(new_list[line+1][column] - value) > 128:
                    contrasting_pixels += 1
                elif abs(new_list[line][column-1] - value) > 128:
                    contrasting_pixels += 1

            elif line == 199 and column == 0:
                if abs(new_list[line-1][column] - value) > 128:
                    contrasting_pixels += 1
                elif abs(new_list[line][column+1] - value) > 128:
                    contrasting_pixels += 1

            elif line == 199 and column == 319:
                if abs(new_list[line-1][column] - value) > 128:
                    contrasting_pixels += 1
                elif abs(new_list[line][column-1] - value) > 128:
                    contrasting_pixels += 1

            elif line == 0:
                if abs(new_list[line][column+1] - value) > 128:
                    contrasting_pixels += 1
                elif abs(new_list[line][column-1] - value) > 128:
                    contrasting_pixels += 1
                elif abs(new_list[line+1][column] - value) > 128:
                    contrasting_pixels += 1

            elif column == 0:
                if abs(new_list[line+1][column] - value) > 128:
                    contrasting_pixels += 1
                elif abs(new_list[line-1][column] - value) > 128:
                    contrasting_pixels += 1
                elif abs(new_list[line][column+1] - value) > 128:
                    contrasting_pixels += 1

            elif line == 199:
                if abs(new_list[line-1][column] - value) > 128:
                    contrasting_pixels += 1
                elif abs(new_list[line][column-1] - value) > 128:
                    contrasting_pixels += 1
                elif abs(new_list[line][column+1] - value) > 128:
                    contrasting_pixels += 1

            elif column == 319:
                if abs(new_list[line-1][column] - value) > 128:
                    contrasting_pixels += 1
                elif abs(new_list[line+1][column] - value) > 128:
                    contrasting_pixels += 1
                elif abs(new_list[line][column-1] - value) > 128:
                    contrasting_pixels += 1

            else:
                if abs(new_list[line-1][column] - value) > 128:
                    contrasting_pixels += 1
                elif abs(new_list[line+1][column] - value) > 128:
                    contrasting_pixels += 1
                elif abs(new_list[line][column-1] - value) > 128:
                    contrasting_pixels += 1
                elif abs(new_list[line][column+1] - value) > 128:
                    contrasting_pixels += 1

    with open("results.txt", "a") as file:
                file.write("10.3\n")
                file.write(f"The number of contrasting pixels: {contrasting_pixels}\n")


if __name__ == "__main__":
    main()
