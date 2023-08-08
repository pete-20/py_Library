from sys import argv
from _.db import Database

# TD:
# add a function allowing to add a table into db
# add a function to modify data in a row
# create an api to show: /books /category /authors
# create an end point to save a new entry into database
# change database to Postgresql
# install Docker&DockerComposer
# use git to put everything into a new branch

print(argv)


if len(argv) == 2 and argv[1] == 'setup':
    Library = Database('Library')
    Library.create_table('''CREATE TABLE library
                           (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            category TEXT, book TEXT, author TEXT,
                            pages INTEGER, status TEXT)'''
                         )

if len(argv) == 2 and argv[1] == 'add':
    Library = Database('Library')
    Library.insert('library', None, 'learning',
                   'Algortymy ilustrowany przewodnik', '?', '?', 'In progress')

if len(argv) == 3 and argv[1] == 'list':
    print(f'Lista linków z kategorii: {argv[2]}')
    category = argv[2]
    db = Database('library')
    links = db.fetch_all('library', category=category)
    for link in links:
        print(link[2])

if len(argv) == 3 and argv[1] == 'delete':
    Library = Database('Library')
    Library.delete("Library", argv[2])

if len(argv) == 5 and argv[1] == 'update':

    # main.py update author Aditya Bhargava WHERE id=1
    Library = Database('Library')
    Library.update("Library", argv[2], argv[3], argv[4])
