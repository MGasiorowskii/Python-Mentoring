dictt ={"a": 3, "b": 1, "c": 10, "d": 15, "e": 20}
new_dictt = {}


# dictt.keys() = dictt
# dictt.values()
# dictt.itesm()
for key, value in dictt.items():
    new_dictt[value] = key

print(new_dictt)
