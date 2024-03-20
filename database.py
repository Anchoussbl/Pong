import sqlite3
import contextlib
import os

class DataBase:
    def __init__(self, name="record_pong.db"):
        self.filename = name
        self.insert_query = """INSERT INTO Scores (Name, Score)
                           VALUES (?, ?); """
        self.update_query = """UPDATE Scores 
                               SET Score=?
                               WHERE Name=?;
        """
        if not os.path.exists(self.filename):
            self.create()

    def create(self):
        create_table = """CREATE TABLE Scores (
                   id INTEGER PRIMARY KEY,
                   Name TEXT,
                   Score Integer
                   );
        """
        with contextlib.closing(sqlite3.connect(self.filename)) as con:
            with con:
                with contextlib.closing(con.cursor()) as cur:
                    cur.execute(create_table)
                    cur.execute(self.insert_query, ("Player1", 0))
                    cur.execute(self.insert_query, ("Player2", 0))

    def load(self):
        result = {}
        with contextlib.closing(sqlite3.connect(self.filename)) as con:
            with con:
                with contextlib.closing(con.cursor()) as cur:
                    cur.execute('SELECT Name, Score FROM Scores;')
                    res = cur.fetchall()  # -> [('Player1', 10), ('Player2', 0)]
                    for row in res:
                        result[row[0]] = row[1]
        return result

    def store(self, values):
        data = ((values["Player1"], "Player1"),
                (values["Player2"], "Player2"))
        with contextlib.closing(sqlite3.connect(self.filename)) as con:
            with con:
                with contextlib.closing(con.cursor()) as cur:
                    for row in data:
                        cur.execute(self.update_query, row)
