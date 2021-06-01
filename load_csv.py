from pprint import pprint
import sqlite3


with open(file=r'data/users.csv', mode='r') as users_file:
    users_list = [i.rstrip('\n').rstrip(',,,').split(',') for i in users_file]
    pprint(users_list)


try:
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    print('Successful connection to DB!')

    pprint(users_list[1:])
    
    cursor.executemany(
        """
        INSERT INTO auth_user (id, username, email)
        VALUES (?, ?, ?)
        """, [lst[:3] for lst in users_list[1:]]
    )
    cursor.close()
except Exception as e:
    print(e)
finally:
    if connection:
        connection.close()
        print('Connection to DB was closed!')
