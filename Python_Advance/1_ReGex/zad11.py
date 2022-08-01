import re


def main():

    txt = ["#ab4", "#AB4B72", "#ab43", "#aaaaaaaaa", "#ahl"]

    for text in txt:
        match = re.findall(r"(#[a-fA-F\d]{6}|#[a-fA-F\d]{3})", text)

        if text in match:
            print(text)


if __name__ == "__main__":
    main()
