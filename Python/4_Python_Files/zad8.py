import json


def revers_dict(**kwargs) -> dict[str, str]:

    new_dict = {}
    for key, value in kwargs.items():
        new_dict[value] = key

    return new_dict


def main():

    dictionary = {'The Sensual World': 'Kate Bush', 'Shaday': 'Ofra Haza', 'Achtung Baby': 'U2',
                  'Aion': 'Dead Can Dance', 'Invisible Touch': 'Genesis'}

    data = revers_dict(**dictionary)
    with open("output.json", "w") as outfile:
        json.dump(data, outfile)


if __name__ == "__main__":
    main()
