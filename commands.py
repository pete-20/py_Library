from db import Database


def func_fetchall(table_name: str):
    db = Database('test')
    links = db.fetch_all(table_name)
    return links


def func_add(table, category, book, author, pages, status):
    db = Database('test')
    db.insert(table, category, book, author, pages, status)


def func_category(table_name: str):
    db = Database('test')
    links2 = db.fetch_cat(table_name)
    return links2


def func_serial(table, column):
    db = Database('test')
    db.dupa(table, column)


def create_table(table_name):
    db = Database('test')
    db.create_table('''CREATE TABLE IF NOT EXISTS library
                    (id SERIAL PRIMARY KEY,
                    category TEXT, book TEXT, author TEXT,
                    pages INTEGER, status TEXT, dupa SERIAL)'''
                    )
