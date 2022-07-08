value_1 = int(input("Podaj I wartość: "))
value_2 = int(input("Podaj II wartość: "))
value_3 = int(input("Podaj III wartość: "))

if value_1 >= value_2 and value_1 >= value_3:
    print(f"największa wartość to {value_1}")
elif value_2 >= value_1 and value_2 >= value_3:
    print(f"największa wartość to {value_2}")
elif value_3 >= value_2 and value_3 >= value_1:
    print(f"największa wartość to {value_3}")