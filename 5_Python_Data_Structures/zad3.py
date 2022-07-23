dictt ={"a": 3, "b": 1, "c": 10, "d": 15, "e": 20}
new_dictt = {}

for key, value in zip(dictt.keys(), dictt.values()):
    new_dictt[value] = key

print(new_dictt)
