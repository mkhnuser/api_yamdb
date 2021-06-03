"""
Таблицы, в которые происходит загрузка:
    category,
    genre
"""
from pprint import pprint
import sqlite3


def parse_csv(path):
    """
    Извлекает данные из data/.
    Возвращает коллекцию вложенных списков вида:
    [[row1], [row2], [row3], ...]
    """
    # users.csv - другой формат (,,, в конце)
    if path != 'data/users.csv':
        with open(file=path, mode='r') as f:
            list_ = [i.rstrip('\n').split(',') for i in f]

    with open(file=path, mode='r') as f:
        list_ = [i.rstrip('\n').rstrip(',,,').split(',') for i in f]

    return list_

def load_csv(table, list_):
    """
    Загружает информацию в базу данных:
        table - таблица, в которую загружаются данные;
        fields - колонки, которые будут использованы;
        to_db - строки, которые будут отправлены;
    """
    try:
        fields = ', '.join(list_[:1][0])
        to_db = list_[1:]

        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        print(f'Successful connection to DB {table}!')

        query = f"""
            INSERT INTO {table}
            ({fields})
            VALUES ({', '.join(['?']*len(to_db[0]))});
        """
        print(query)

        cursor.executemany(
            query, to_db
        )
        connection.commit()
        connection.close()
    except Exception as e:
        print(e)
    finally:
        if connection:
            connection.close()
            print(f'Connection to DB {table} was closed!')


def main():
    try:
        load_csv(
            table='titles_category',
            list_=parse_csv('data/category.csv'),
        ) 
        load_csv(
            table='titles_genre',
            list_=parse_csv('data/genre.csv')
        )
    except Exception as e:
        print(e)
    else:
        print('Data was exported. No issues were detected')


if __name__ == '__main__':
    main()
