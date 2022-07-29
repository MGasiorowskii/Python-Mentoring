def main():
    with open("example_1.txt", encoding="utf-8") as plik:
        plik.tell()
        plik.seek(43)
        print(plik.read(1))


if __name__ == "__main__":
    main()