from typing import Any
people: dict[str, [str, str]] = {"11111111111": {"eye_color": "green", "name": "Karol", "surname": "Karolak", "age": 22},
          "22222222222": {"eye_color": "black", "name": "Marcin", "surname": "Smith", "age": 23},
          "33333333333": {"eye_color": "brown", "name": "Anna", "surname": "Kowalska", "age": 24},
          "44444444444": {"eye_color": "blue", "name": "Kamil", "surname": "Lato", "age": 25},
          "55555555555": {"eye_color": "green", "name": "Mateusz", "surname": "Kania", "age": 26}}

print(people["11111111111"]["eye_color"])


for PESEL in people.values():

    PESEL.update({"mother_name": "Irena"})

key_to_remove = []
for PESEL in people.keys():
    if PESEL[-1] == "1":
        key_to_remove.append(PESEL)

for element in key_to_remove:
    people.pop(element)

for PESEL, info in zip(people.keys(), people.values()):
    print(f"PESEL :\t{PESEL}")

    for name, value in zip(info.keys(), info.values()):
        print(f"{name} :{value}")

    print()
