import re


def main():
    txt1 = "sshis"
    txt2 = "hiss"

    plain_txt1 = re.search(r's{2,}$', txt1)
    plain_txt2 = re.search(r's{2,}$', txt2)

    if plain_txt1:
        print("End of string contains 2 or more letter 's' ")
    else:
        print("String contains other signs")

    if plain_txt2:
        print("End of string contains 2 or more letter 's' ")
    else:
        print("String contains other signs")


if __name__ == "__main__":
    main()
