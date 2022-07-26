albums = {'The Sensual World': 'Kate Bush', 'Shaday': 'Ofra Haza', 'Achtung Baby': 'U2', 'Aion': 'Dead Can Dance',
          'Invisible Touch': 'Genesis'}

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
        album = input("Give a album: ").lower()
        artist = input("Give a artis: ").lower()
        albums[album] = artist

    elif user_choice == 2:
        album = input("Input the name of album: ")
        print(f"Performer of the album {album} is {albums[artist]}")

    elif user_choice == 3:
        album = input("Input a album to remove from dictionary: ").lower()
        albums.pop(album)

    elif user_choice == 4:
        print(albums)

    elif user_choice == 5:
        break

    else:
        print("Incorrect number!")
