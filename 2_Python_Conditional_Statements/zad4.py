value_1 = input("Player 1 - Choose one (paper, stone albo shears): ")
value_2 = input("Player 2 - Choose one (paper, stone albo shears): ")

if (value_1 == "paper" or value_1 == "stone" or value_1 == "shears") and \
        (value_2 == "paper" or value_2 == "stone" or value_2 == "shears"):

    if value_1 == value_2:
        print("DRAW!")

    elif (value_1 == "paper" and value_2 == "shears") or\
            (value_1 == "stone" and value_2 == "paper") or \
            (value_1 == "shears" and value_2 == "stone"):
        print("WIN player 2")
    else:
        print("WIN player 1")

else:
    print("Invalid information!")