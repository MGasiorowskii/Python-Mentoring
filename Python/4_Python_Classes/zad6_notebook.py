from __future__ import annotations
import time
import datetime


class Notebook:
    def __init__(self):
        self.list_of_notes = []

    def __len__(self):
        return len(self.list_of_notes)

    def __getitem__(self, item):
        return self.list_of_notes[item]


    def display_everything(self) -> None:
        print("Your Notes:")
        for index, note in enumerate(self.list_of_notes, 1):
            print(f"{index}. {note}")

    def add_new(self, author: str, content: str) -> None:
        new_note = Note(author, content)

        if not self.list_of_notes:
            self.list_of_notes.append(new_note)
            return

        for note in self.list_of_notes:
            if note.author == author and note.content == content:
                print("Such a note already exists")
                return

        self.list_of_notes.append(new_note)

    def add_note(self, new_note: Note) -> None:
        if not self.list_of_notes:
            self.list_of_notes.append(new_note)
            return

        for note in self.list_of_notes:
            if note.author == new_note.author and note.content == new_note.content:
                print("Such a note already exists")
                return
        self.list_of_notes.append(new_note)

    def count_notes(self) -> None:
        print(f"Notebook contains {len(self)} notes")


class Note:
    def __init__(self, author_: str, content_: str) -> None:
        self.author = author_
        self.content = content_
        self.hour = datetime.datetime.now().hour
        self.minutes = time.localtime()[4]

    def __str__(self):
        return f"{self.author}: '{self.content}' at {self.hour}:{self.minutes}"


def main():

    nb = Notebook()
    nb.add_new("Bartek", "Dokonczyc instrukcje")
    nb.display_everything()
    print()

    n1 = Note("Andrii", "Sprawdzic instrukcje")
    nb.add_note(n1)
    nb.display_everything()
    print()

    nb.add_new("Bartek", "Dokonczyc instrukcje")

    nb.count_notes()


    print(len(nb))

    print(nb[3])


if __name__ == "__main__":
    main()
