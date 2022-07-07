liczbaKotow = int(input("Ile kotów ma Ala? "))
print(f"Dzisiaj Ala znalazła jeszcze 3 koty na ulicy")
phrase = f"Teraz Ala ma już {liczbaKotow+3} kotów"

print(phrase)
print(phrase.replace(" ", ","))
print(phrase.replace(" ", "\n"))

if not phrase.islower():
    phrase = phrase.lower()

print(phrase)
print(phrase.capitalize())
