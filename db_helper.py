import sqlite3
import os
from helper import dict_to_query

def query(Column, Table, Conditions = "") -> list:
    db = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.db"))
    cursor = db.cursor()
    query = f"SELECT {Column if Column != "" else "*"} FROM {Table} WHERE {Conditions if Conditions != "" else "1"}"
    cursor.execute(query)

    return cursor.fetchall()

def custom_query(CustomQuery: str):
    db = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.db"))
    cursor = db.cursor()
    cursor.execute(CustomQuery)
    return cursor.fetchall()

def insert(Table: str, Values: tuple) -> None:
    db = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.db"))
    cursor = db.cursor()
    query = f"INSERT INTO {Table} VALUES {str(Values)}"
    cursor.execute(query)
    db.commit()

def update(Table: str, Values, Condition: str):
    db = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.db"))
    cursor = db.cursor()
    query = f"UPDATE {Table} SET {str(dict_to_query(Values)) if isinstance(Values, dict) else Values} WHERE {Condition}"
    cursor.execute(query)
    db.commit()
def delete(Table: str, Condition: str):
    db = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.db"))
    cursor = db.cursor()
    query = f"DELETE FROM {Table} WHERE {Condition}"
    cursor.execute(query)
    db.commit()

if __name__ == "__main__":
    print(query("*", "Autores", "Edad = 99"))