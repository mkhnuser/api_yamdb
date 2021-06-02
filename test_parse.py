import sqlite3
from pprint import pprint


try:
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    print('Successful connection to DB!')

    sqlite_select_tables = (
        """
        SELECT name FROM sqlite_master WHERE type='table';
        """
    )
    cursor.execute(sqlite_select_tables)
    record = cursor.fetchall()

    for row in record:
        print(row)

    cursor.close()
except Exception as e:
    print(e)
finally:
    if connection:
        connection.close()
        print('Connection to DB was closed!')
