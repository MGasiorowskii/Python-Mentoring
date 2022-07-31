import re


def main():
    txt = ["Python should match", "unique New AYork", "Regular Expressions", "ha haha", "ALOHkA"]

    for text in txt:
        split_txt = re.sub(r'[^B-z]', "", text)
        if len(split_txt) >= 6:
            print(text)


if __name__ == "__main__":
    main()
