import random

top_range = int(input("Input top range: "))
bottom_range = int(input("Input bottom range: "))
points = top_range - bottom_range

computer_number = random.randint(bottom_range, top_range)
print("Computer has drawn a number ... ")
user_number = -1
while user_number != computer_number:
    user_number = int(input("Guess the number: "))

    if user_number < computer_number:
        print("You input too small number")
    elif user_number > computer_number:
        print("You input too big number")
    points -= 1

print(f"Congratulation! You earned {points} points!")
