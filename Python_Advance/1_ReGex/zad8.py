import re


def main():

    txt = "2 cats and 3 dogs"

    match = re.findall(r"\d", txt)
    print(match)


if __name__ == "__main__":
    main()
