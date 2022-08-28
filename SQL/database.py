import sqlite3
import datetime


class Database:
    def __init__(self) -> None:
        self.con = sqlite3.connect("notebook.db")

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS Notebook
                (note_name TEXT PRIMARY KEY,
                content TEXT,
                date_of_creation timestamp)"""
        self.con.execute(query)

    def add_note(self, note_name: str, content: str) -> None:
        date_of_creation = datetime.datetime.now()
        query = f"INSERT INTO Notebook(note_name, content, date_of_creation) VALUES(?, ?, ?)"
        self.con.execute(query, (note_name, content, date_of_creation))

    def preview_table(self) -> None:
        query = f"SELECT * FROM Notebook"
        results = self.con.execute(query).fetchall()
        print(results)

    def delete_note(self, note_name: str) -> None:
        query = f"DELETE FROM Notebook WHERE note_name = '{note_name}'"
        self.con.execute(query)

    def __del__(self):
        self.con.commit()
        self.con.close()
