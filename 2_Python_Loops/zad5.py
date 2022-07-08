divider = int(input("Input divider: "))

for num in range(50, 101):

    if num % divider == 0:
        print(f"{num}", end=" ")
