from db import Database


# 1
def func_fetchall(table_name: str):
    db = Database('test')
    links = db.fetch_all(table_name)
    return links


# 2
def func_add(table, category, book, author, pages, status):
    db = Database('test')
    db.insert(table, category, book, author, pages, status)


# 3
def func_category(table_name: str, category: str):
    db = Database('test')
    links2 = db.fetch_cat(table_name, category)
    return links2


# 4
def create_table(table_name):
    db = Database('test')
    db.create_table('''CREATE TABLE IF NOT EXISTS library
                    (id SERIAL PRIMARY KEY,
                    category TEXT, book TEXT, author TEXT,
                    pages INTEGER, status TEXT)'''
                    )


# 5
def func_delete(table_name, id: int):
    db = Database('test')
    db.delete(table_name, id)


# 6
def func_column_unique(table, book):
    db = Database('test')
    db.change_column_unique(table, book)


# 7
def func_new_column(table, column_name):
    db = Database('test')
    db.add_new_column(table, column_name)


# 8
def func_update(table, key: str, value, id):
    db = Database('test')
    db.update(table, key, value, id)


# 9
def func_category_distinct(table):
    db = Database('test')
    dis_cat = db.category_distinct(table, 'category')
    print(dis_cat)
    for a in dis_cat:
        print(a[0])
    return dis_cat
