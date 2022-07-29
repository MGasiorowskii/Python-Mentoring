import random

numbers = set()
for i in range(15):
    numbers.add(random.randint(5, 120))
print(numbers)

even_numbers = set()
for number in range(121):
    if number % 2 == 0:
        even_numbers.add(number)
print(even_numbers)

numbers -= even_numbers
print(numbers)
