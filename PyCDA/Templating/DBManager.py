import sqlite3 as db


class DBManager:
    def __init__(self):
        try:
            self.connection = db.connect("PyCDA/Templating/dbs/CDA_TEMPLATES")
            self.cursor = self.connection.cursor()
        except db.Error as Error:
            raise Error

    def __del__(self):
        if self.connection:
            self.connection.close()

    def fetch(self, query: str) -> list[tuple]:
        self.cursor.execute(query)
        return self.cursor.fetchall()
