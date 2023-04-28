import sqlite3


class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._conn = sqlite3.connect("profile.db")
            cls._instance._conn.row_factory = sqlite3.Row
            cls._instance._cursor = cls._instance._conn.cursor()
        return cls._instance

    def get_connection(self):
        return self._conn

    def __del__(self):
        self._conn.close()
