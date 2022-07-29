import re


def main():
    txt1 = "devs_mentoring"
    txt2 = "Mgasiorowskii97"

    plain_txt1 = re.search(r'[a-z]_[a-z]', txt1)
    plain_txt2 = re.search(r'[a-z]_[a-z]', txt2)

    if plain_txt1:
        print("String contains string of signs [a-z]_[a-z] ")
    else:
        print("String contains other signs")

    if plain_txt2:
        print("String contains string of signs [a-z]_[a-z] ")
    else:
        print("String contains other signs")


if __name__ == "__main__":
    main()
