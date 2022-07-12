ANG_dictionary = {"fancy": "to want to have or do something",
                  "adequate": "good enough, but not very good",
                  "son": "your male child"}

intro = """
MENU:
1 - Add new word to dictionary
2 - Find definitions of word
3 - Remove word from dictionary
4 - Print the dictionary
5 - End program
"""

while True:
    print(intro)
    user_choice = int(input("Choose a command: "))

    if user_choice == 1:
        word = input("Give a word: ").lower()
        definition = input("Give a definition: ").lower()
        ANG_dictionary.update(word, definition)

    elif user_choice == 2:
        word = input("Give a word: ").lower()
        definition = ANG_dictionary.get(word, "Lack of definition in dictionary").lower()
        print(f"Definition of this word {word}: '{definition}' ")

    elif user_choice == 3:
        word = input("Input a word to remove from dictionary: ").lower()
        ANG_dictionary.pop(word, "Lack of this word in dictionary")     #???

    elif user_choice == 4:
        print(ANG_dictionary)

    elif user_choice == 5:
        break

    else:
        print("Incorrect number!")
