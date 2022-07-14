num_1 = int(input("Input I number: "))
num_2 = int(input("Input II number: "))

if (num_1 % 2 == 0) or (num_2 % 2 == 0):
    print("One of the following numbers is even")
else:
    print("Both of numbers are odd")