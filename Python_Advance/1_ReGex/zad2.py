import re


def main():
    txt1 = "011"
    txt2 = "Mgasiorowskii97"

    plain_txt1 = re.match(r'^0|^b', txt1)
    plain_txt2 = re.match(r'^0|^b', txt2)

    if plain_txt1:
        print("First sign of string is '0' or 'b' ")
    else:
        print("String contains other signs")

    if plain_txt2:
        print("First sign of string in '0' or 'b' ")
    else:
        print("String contains other signs")


if __name__ == "__main__":
    main()
