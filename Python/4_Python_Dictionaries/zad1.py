albums = {'The Sensual World': 'Kate Bush', 'Shaday': 'Ofra Haza', 'Achtung Baby': 'U2', 'Aion': 'Dead Can Dance',
          'Invisible Touch': 'Genesis'}

user_input = input("Input the name of album: ")

if user_input in albums:
    print(f"Performer of the album {user_input} is {albums[user_input]}")
else:
    print("Lack of data")
