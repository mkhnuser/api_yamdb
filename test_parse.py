"""
Цель этого файла - заменить sqlite3 client. Здесь можно писать SQL запросы.
"""
import sqlite3
from pprint import pprint


try:
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()

    sqlite_select_tables = (
        """
        SELECT name FROM sqlite_master WHERE type='table';
        """
    )
    cursor.execute(sqlite_select_tables)
    record = cursor.fetchall()

    for row in record:
        pprint(row)

    cursor.close()
except Exception as e:
    print(e)
finally:
    if connection:
        connection.close()
