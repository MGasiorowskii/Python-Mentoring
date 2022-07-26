power = int(input("Input the power of the number 2: "))

for num in range(power+1):
    result = 2**num
    print(f"{result}", end=" ")