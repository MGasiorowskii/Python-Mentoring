print("a)")
print("*" * 10)

print("b)")
for i in range(1, 5):
    print("*" * i)

print("c)")
for i in range(1, 4):
    print("*" * 3)

print("d)")
stars = "*"
print(stars.center(10))

for i in range(4):
    for j in range(2):
        stars += "*"

    print(stars.center(10))

'''
print("*".center(10,"-"))
print("***".center(10,"-"))
print("*****".center(10,"-"))
print("*******".center(10,"-"))
print("*********")
'''
