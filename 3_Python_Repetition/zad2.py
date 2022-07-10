number = int(input("Input any number: "))
numbers = []

for num in range(number):
    numbers.append(num+1)

print(numbers)
print(sum(numbers))