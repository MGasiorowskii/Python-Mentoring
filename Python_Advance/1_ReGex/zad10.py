import re


def main():

    txt = "2019-03-11: 23.5, 19/03/12: 12.7, 2019.03.13: 11.1, 2019-marzec-14: 14.3"

    match = re.findall(r'\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{2}|\d{4}.\d{2}.\d{2}|\d{4}-\w+-\d{2}', txt)

    print(match)


if __name__ == "__main__":
    main()
