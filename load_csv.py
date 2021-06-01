import sqlite3


with open(file=r'data/users.csv', mode='r') as users_file:
    for i in users_file:
        print(i.rstrip('\n').rstrip(',,,'))

    users_list = [i.rstrip('\n').rstrip(',,,') for i in users_file]
"""
try:
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    print('Successful connection to DB!')

    sqlite_select = 'SELECT sqlite_version();'
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
"""
