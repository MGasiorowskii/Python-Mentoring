import random

score = [12, 1, 45, 76, 50, 23]

for number in score:

    if 1 <= number <= 49:
        pass
    else:
        new_number = random.randint(1, 49)
        print(f"Incorrect value {number} has been changed to {new_number}")
        number = new_number

print(score)
