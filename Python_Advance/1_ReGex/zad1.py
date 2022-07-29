import re


def main():
    txt1 = "Devs-Mentoring 2011"
    txt2 = "Mgasiorowskii97"

    plain_txt1 = re.sub(r'\d|[A-z]', "", txt1)
    plain_txt2 = re.sub(r'\d|[A-z]', "", txt2)

    if plain_txt1:
        print("String contains other signs")
    else:
        print("String contains only signs from [A-z][0-9]")

    if plain_txt2:
        print("String contains other signs")
    else:
        print("String contains only signs from [A-z][0-9]")


if __name__ == "__main__":
    main()
