import re


def main():

    txt = "username@companyname.com"

    match = re.match(r"(\w*)@(\w*).([A-z]*)", txt)
    print(f"Name of company: {match.group(2)}")


if __name__ == "__main__":
    main()
