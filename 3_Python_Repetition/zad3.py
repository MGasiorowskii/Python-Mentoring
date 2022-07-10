numbers = []

for i in range(10):
    numbers.append(int(input(f"Input number {i+1}: ")))

for num in numbers:
    if num % 2 == 0:
        print(num, end=" ")
