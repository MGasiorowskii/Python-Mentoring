import sqlite3


class Database:
    def __init__(self, path):
        self.con = sqlite3.connect(path)

    def create_table(self):
        query = "CREATE TABLE IF NOT EXISTS Customers(id INTEGER PRIMARY KEY, name TEXT NOT NULL, surname TEXT NOT NULL, date_joined DATE NOT NULL);"
        self.con.execute(query)

    def add_to_customers(self, name, surname, date_joined):
        query = "INSERT INTO Customers(name, surname, date_joined) VALUES(?, ?, ?)"
        self.con.execute(query, (name, surname, date_joined))

    def preview_table(self, table_name):
        query = f"SELECT * FROM {table_name}"
        results = self.con.execute(query).fetchall()
        print(results)

    def modify_tabel_add(self, table_name: str, column_name: str, column_type: str) -> None:
        query = f"ALTER TABLE {table_name} ADD {column_name} {column_type}"
        self.con.execute(query)

    def modify_tabel_set(self, table_name: str, column_name: str, column_type: str) -> None:
        query = f"ALTER TABLE {table_name} ALTER COLUMN {column_name} SET {column_type}"
        self.con.execute(query)

    def modify_tabel_rename(self, table_name: str, original_column_name: str, new_column_name: str) -> None:
        query = f"ALTER TABLE {table_name} RENAME COLUMN {original_column_name} TO {new_column_name}"
        self.con.execute(query)

    def modify_tabel_drop(self, table_name: str, column_name: str, column_type: str) -> None:
        query = f"ALTER TABLE {table_name} ALTER COLUMN {column_name} DROP {column_type}"
        self.con.execute(query)

    def update_tabel(self, tabel_name: str, value_equal: str, where_condition: str) -> None:
        query = f"UPDATE {tabel_name} SET {value_equal} WHERE {where_condition}"
        self.con.execute(query)

    def delete_data(self, tabel_name: str, where_condition: str) -> None:
        query = f"DELETE FROM {tabel_name} WHERE {where_condition}"
        self.con.execute(query)

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        if isinstance(exc_value, Exception):
            self.con.rollback()
        else:
            self.con.commit()

        self.con.close()
        