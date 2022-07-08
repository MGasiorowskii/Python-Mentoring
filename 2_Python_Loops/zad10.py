num = int(input("Input number: "))

dividers = []

for div in range(1, num):
    if (num % div) == 0:
        dividers.append(div)

if sum(dividers) == num:
    print(dividers)
    print("Your number is perfect!")
else:
    print("Your number is ugly :c ")
