import sqlite3

from database import Database


class Notebook:
    def __init__(self) -> None:
        self.__is_running = True
        self.db = Database()
        self.db.create_table()
        self.choices = {
            1: self.add_note,
            2: self.preview_tabel,
            3: self.delete_note,
            4: self.quit
        }
        self.initialize()

    def initialize(self) -> None:
        while self.__is_running:
            self.show_menu()
            self.get_and_execute_choice()

    def show_menu(self) -> None:
        menu = """
    1. Add Note
    2. Show Notes
    3. Delete Note
    4. Exit
        """
        print(menu)

    def get_and_execute_choice(self) -> None:
        user_choice = int(input("Choose what you want do: "))
        try:
            self.choices.get(user_choice, self.show_error)()

        except sqlite3.Error as error:
            print("Error while working with SQLite - try again; error type: ", error)

    def show_error(self) -> None:
        print("Incorrect choice - Try again")

    def quit(self) -> None:
        self.__is_running = False
        del self.db

    def add_note(self) -> None:
        note_name = input("Input note name to add: ")
        content = input("Input content of the note: ")

        self.db.add_note(note_name, content)

    def preview_tabel(self) -> None:
        self.db.preview_table()

    def delete_note(self) -> None:
        note_name = input("Input note name to delete: ")

        self.db.delete_note(note_name)


def main():
    Notebook()


if __name__ == "__main__":
    main()
