import re


def main():

    txt = ["<span>Yowza! That’s a great regular expression.</span>",
           "<p>Learn about regular expressions here.</p>   <p>You are going to love them!</p>", "I'm not HTML!!",
           "<p>Incomplete HTML"]

    for text in txt:

        match = re.findall(r"<\w*>.*?</\w*>", text)

        [print(code) for code in match]


if __name__ == "__main__":
    main()
