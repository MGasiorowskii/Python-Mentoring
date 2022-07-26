side_1 = int(input("Podaj I bok trójkąta: "))
side_2 = int(input("Podaj II bok trójkąta: "))
side_3 = int(input("Podaj III bok trójkąta: "))

if side_1**2 + side_2**2 == side_3**2:
    print("Trójkąt ten jest prostokątny")
elif side_1**2 + side_3**2 == side_2**2:
    print("Trójkąt ten jest prostokątny")
elif side_2**2 + side_3**2 == side_1**2:
    print("Trójkąt ten jest prostokątny")
else:
    print("Trójkąt ten nie jest prostokątny")