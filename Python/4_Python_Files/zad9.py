import json


intro ="""
Interface Status
================================================================================
DN                                                 Description           Speed    
MTU  
"""


with open("data.json") as f:
    data = json.load(f)

for row in data['imdata']:
    dn = row['l1PhysIf']['attributes']['dn']
    description = row['l1PhysIf']['attributes']['descr']
    speed = row['l1PhysIf']['attributes']['speed']
    mtu = row['l1PhysIf']['attributes']['mtu']

    # print(intro)
    print("Interface Status")
    print("=" * 80)
    print("DN", end="")
    print(" " * 49, end="")
    print("Description", end="")
    print(" " * 11, end="")
    print("Speed")
    print("{:<7}{:>11}{:>25}\n{}\n".format(dn, description, speed, mtu))


