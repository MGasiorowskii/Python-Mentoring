liczbaKotow = int(input("Ile kotów ma Ala? "))
print(f"Dzisiaj Ala znalazła jeszcze 3 koty na ulicy")
str = f"Teraz Ala ma już {liczbaKotow+3} kotów"
print(str)
print(str.replace(" ",","))
print(str.replace(" ","\n"))

if not str.islower():
    str = str.lower()

print(str)
print(str.capitalize())
