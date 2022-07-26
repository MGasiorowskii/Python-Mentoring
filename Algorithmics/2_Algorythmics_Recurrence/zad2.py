vowels = ['a', 'e', 'i', 'o', 'u', 'y']

"""
def rec_vowels(word: str) -> dict[str, int]:
    freq = {}
    for letter in word:
        if letter in vowels:
            if letter in freq.keys():
                freq[letter] += 1
            else:
                freq[letter] = 1
    return freq
"""


def rec_vowels(word: str, result: dict) -> dict[str, int]:

    if not word:
        return result

    letter = word[-1]
    if letter in vowels:
        if letter in result.keys():
            result[letter] += 1
        else:
            result[letter] = 1

    return rec_vowels(word[:-1], result)


def main():
    phrase = "baadace"
    result = {}

    print(rec_vowels(phrase, result))


if __name__ == "__main__":
    main()
