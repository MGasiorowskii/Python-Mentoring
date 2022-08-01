import re


def main():

    txt = ["123,2341515132135", "-10", "18-12", "123,"]

    for text in txt:

        match = re.search(r"\d*,\d+|\d+|-\d+", text)
        if match.group() == text:
            print(text)


if __name__ == "__main__":
    main()
