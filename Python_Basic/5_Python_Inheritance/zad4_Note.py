from __future__ import annotations
from typing import Any


# jak podchodzic do towrzeni programu jak wyglada proces
class Menu:
    def show(self):
        menu = """
        1. Add Note
        2. Add Card
        3. Show all Notes
        4. Show all Cards
        5. Exit
        """
        print(menu)

    def get_choice(self) -> int:
        return int(input("Choose what you want do: "))


class NotesSubManager:
    def __init__(self) -> None:
        self.notes = []

    def add_note(self) -> None:
        note = input("Write the note: ")
        self.notes.append(note)

    def show_notes(self) -> None:
        print(self.notes)


class CardsSubManager:
    def __init__(self) -> None:
        self.cards = []

    def add_card(self) -> None:
        card = input("Write the card: ")
        self.notes.append(card)

    def show_cards(self) -> None:
        print(self.cards)


class Manager(Menu, CardsSubManager, NotesSubManager):
    def __init__(self) -> None:
        CardsSubManager.__init__(self)
        NotesSubManager.__init__(self)
        self.start()

    def start(self) -> None:
        """Method printing Main Menu, and execute program"""
        self.show_menu()
        self.execute()

    def show_menu(self) -> None:
        """helper method to show menu"""
        self.show()

    def execute(self) -> None:
        user_choice = self.get_choice()
        choices = {
            1: self.add_note(),
            2: self.add_card(),
            3: self.show_notes(),
            4: self.show_cards(),
            5: exit()
        }
        if user_choice in choices:
            choices.get(user_choice)
        else:
            print("Inccorect Value")
        # if user_choice == 1:
        #     self.add_note()
        # elif user_choice == 2:
        #     self.add_card()
        # elif user_choice == 3:
        #     self.show_notes()
        # elif user_choice == 4:
        #     self.show_cards()
        # elif user_choice == 5:
        #     return

        self.start()


def main():
    p1 = Manager()


if __name__ == "__main__":
    main()
