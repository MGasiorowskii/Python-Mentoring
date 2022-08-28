import sqlite3


def connect_to_db(path):
    con = sqlite3.connect(path)
    return con


def create_table(con):
    query = "CREATE TABLE IF NOT EXISTS Customers(id INTEGER PRIMARY KEY, name TEXT NOT NULL, surname TEXT NOT NULL, date_joined DATE NOT NULL);"
    con.execute(query)
    con.commit()


def add_to_customers(con, name, surname, date_joined):
    query = "INSERT INTO Customers(name, surname, date_joined) VALUES(?, ?, ?)"
    con.execute(query, (name, surname, date_joined))
    con.commit()


def preview_table(con, table_name):
    query = f"SELECT * FROM {table_name}"
    results = con.execute(query).fetchall()
    print(results)


con = connect_to_db("example-database.db")
create_table(con)
add_to_customers(con, 'John', 'Wick', '2000-09-02')
add_to_customers(con, 'James', 'Bond', '2002-05-16')
preview_table(con, 'Customers')
