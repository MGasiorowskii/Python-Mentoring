import json
# TODO "dn", "Description", "SPEED", "MTU",


print("{}".format('DN'))

with open("data.json") as f:
    data = json.load(f)

for row in data['imdata']:
    print(row['l1PhysIf']['attributes']['dn'])
