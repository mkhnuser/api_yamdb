import sqlite3
from pprint import pprint


try:
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()

    sqlite_select_tables = (
        """
        SELECT * FROM sqlite_master WHERE type='table';
        """
    )
    cursor.execute(sqlite_select_tables)
    record = cursor.fetchall()

    for row in record:
        pprint(row)

    cursor.close()
except Exception as e:
    pprint(e)
finally:
    if connection:
        connection.close()
