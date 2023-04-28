from multiprocessing import Pool

from selenium_module import runner
from connect_db import DatabaseConnection

if __name__ == '__main__':
    db = DatabaseConnection()
    conn = db.get_connection()
    cursor = conn.cursor()
    rows = cursor.execute('select * from cookie_profile').fetchall()
    result = [dict(row) for row in rows]

    with Pool(5) as p:
        print(p.map(runner, result))
