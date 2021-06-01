import sqlite3


try:
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    print('Successful connection to DB!')

    sqlite_select = (
        """
        SELECT name FROM sqlite_master WHERE type='table';
        """
    )
    cursor.execute(sqlite_select)
    record = cursor.fetchall()
    print(record)
    cursor.close()
except Exception as e:
    print(e)
finally:
    if connection:
        connection.close()
        print('Connection to DB was closed!')
