import psycopg2


class Database():
    # 1
    def __init__(self, database_name):
        print("\nConnecting to the PostgreSQL\n")
        self.connection = psycopg2.connect(host="db",
                                           database=f'{database_name}',
                                           user="postgres",
                                           password="new_password",
                                           port="5432")
        self.cursor = self.connection.cursor()
        print('PostgreSQL database version:')
        self.cursor.execute('SELECT version()')
        db_version = self.cursor.fetchone()
        print(f"{db_version}\n")

    # 2
    def __del__(self):
        self.connection.close()
        print("\nDatabase connection closed\n")

    # 3
    def create_table(self, sql: str):
        print('Creating a table')
        self.cursor.execute(sql)
        self.connection.commit()
        print('Table has been created')

    # 4
    def insert(self, table, *values):
        print(
            f"INSERT INTO {table} VALUES ({','.join(['%s' for _ in values])})", values)
        self.cursor.execute(
            f"INSERT INTO {table} VALUES (DEFAULT,{','.join(['%s' for _ in values])})", values)
        self.connection.commit()

    # 5
    def fetch_all(self, table):
        self.cursor.execute(f'SELECT * FROM {table} ORDER BY ID;')
        return self.cursor.fetchall()

    # 6
    def fetch_cat(self, table, category):
        self.cursor.execute(
            f"SELECT * FROM {table} WHERE category='{category}';")
        return self.cursor.fetchall()

    # 7
    def delete(self, table, id):
        self.cursor.execute(f"DELETE from {table} WHERE id={id}")
        self.connection.commit()

    # 8
    def update(self, table, key, value, id):
        print(table, key, value, id)
        print(f"UPDATE {table} SET {key}={value} WHERE id={id}")
        self.cursor.execute(f"UPDATE {table} SET {key}='{value}' WHERE id={id}")
        self.connection.commit()

    # 9
    def change_column_unique(self, table, book):
        self.cursor.execute(
            f'ALTER TABLE {table} ADD UNIQUE ({book});'
        )
        self.connection.commit()

    # 10
    def add_new_column(self, table, column_name):
        self.cursor.execute(
            f'ALTER TABLE {table} ADD COLUMN {column_name} TEXT'
        )
        self.connection.commit()

    # 11
    def category_distinct(self, table, coulmn_name):
        self.cursor.execute(f"SELECT DISTINCT {coulmn_name} FROM {table}")
        return self.cursor.fetchall()

    # 12
    def fetch_id(self, table, id):
        self.cursor.execute(f'SELECT * FROM {table} WHERE id={id};')
        return self.cursor.fetchall()
