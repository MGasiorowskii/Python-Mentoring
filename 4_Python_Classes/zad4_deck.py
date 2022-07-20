import random


class Deck:

    def __init__(self):
        self.cards = []
        for figure in Card.figures:
            for number in Card.numbers:
                self.cards.append(Card(number, figure))

        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):

        print(self.cards[-1])
        self.cards.remove(self.cards[-1])


class Card:
    figures = ["clubs", "diamonds", "hearts", "spades"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, value_: str, figure_: str):
        self.value = value_
        self.figure = figure_

    def __str__(self):
        return f"Card number: {self.value}\nCard figure: {self.figure}"


def main():

    my_deck = Deck()
    my_deck.deal()


if __name__ == "__main__":
    main()
