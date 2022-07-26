import random
import time

print("Let's play a game!")

user_score = 0
possible_moves = {1: "heads", 2: "tails"}

while True:
    user_choice = int(input("Choose one: 0 - (end the game), 1 - (heads), 2 - (tails): "))
    computer_choice = random.randint(1, 2)
    print(f"You chose: {possible_moves.get(user_choice)}")

    if user_choice == 0:
        break

    for sec in range(3, 0, -1):
        print(f"{sec}...")
        time.sleep(0.5)

    print(f"Computer chose: {possible_moves.get(computer_choice)}")
    if user_choice == computer_choice:
        user_score += 1
        print(f"WIN, You have {user_score} points")
    else:
        print(f"LOSE, You have {user_score} points")

    input("\nPress any key to continue ...")

print("\nThank you for teh game")
print(f"You've collected {user_score} points")