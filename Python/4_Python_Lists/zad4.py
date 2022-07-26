names = ["Bartosz", "Anna", "Kasia", "Marek"]
messages = ["Nice to meet you", "Welcome", "Have a nice day", "Hi"]

for name, message in zip(names, messages):
    print(f"{message} {name}")
