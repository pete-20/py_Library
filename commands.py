from db import Database


# def func_setup():
#    db = Database('test')


def func_fetchall(table_name: str):
    db = Database('test')
    links = db.fetch_all(table_name)
    print('ABC')
    print(links)
    print('ABC')
    for link in links:
        print(link)
    return links


"""
def func_distinct(table_name: str, column: str):
    db = Database('test')
    links2 = db.fetch_cat(table_name, column)
    print('hahahaha')
    print(links2)
    print('hahahaha')
    for link2 in links2:
        print(link2)
    return links2
"""


def func_add(table, category, book, author, pages, status):
    print('MAM CIE!!!!!!!!!!!!!!!!!!!!!!!')
    print('MAM CIE!!!!!!!!!!!!!!!!!!!!!!!')
    db = Database('test')
    db.insert(table, category, book, author, pages, status)


def func_category(table_name: str):
    db = Database('test')
    links2 = db.fetch_cat(table_name)
    print('WIN_ONLY_WIN')
    print(links2)
    print('WIN_ONLY_WIN')
    for link2 in links2:
        print(link2)
    return links2


def func_serial(table, column):
    db = Database('test')
    db.dupa(table, column)


def create_table(table_name):
    print(table_name)
    db = Database(table_name)
    db.create_table('''CREATE TABLE IF NOT EXISTS library
                    (id SERIAL PRIMARY KEY,
                    category TEXT, book TEXT, author TEXT,
                    pages INTEGER, status TEXT, dupa SERIAL)'''
                    )
