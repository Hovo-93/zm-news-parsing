import random
from datetime import datetime

from connect_db import DatabaseConnection

"""
    Создание базы данных Profile и подключение к ней
"""
db = DatabaseConnection()

conn = db.get_connection()
cursor = conn.cursor()


# Генерируем 15 записей
def generate_fake_data(count):
    for _ in range(count):
        created_at = datetime.now()
        data = (created_at, '', '', '')
        cursor.execute(f"INSERT INTO cookie_profile (created_at,value_cookie,date_time_last_run,count_run"
                       f") VALUES (?,?,?,?)", data)


def create_table():
    """
        Создание таблицы Cookie Profile
    """
    query = '''
     CREATE TABLE if not exists  cookie_profile(
            `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            `created_at` DATETIME NOT NULL,
            `value_cookie` TEXT,
            `date_time_last_run` DATETIME,
            `count_run` INTEGER);
    '''
    cursor.execute(query)


if __name__ == '__main__':
    create_table()
    generate_fake_data(15)
