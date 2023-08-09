import psycopg2


class Database():
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

    def __del__(self):
        self.connection.close()
        print("\nDatabase connection closed\n")

    def create_table(self, sql: str):
        print('Creating a table')
        self.cursor.execute(sql)
        self.connection.commit()
        print('Table has been created')

    def insert(self, table, *values):
        print(
            f"INSERT INTO {table} VALUES ({','.join(['%s' for _ in values])})", values)
        self.cursor.execute(
            f"INSERT INTO {table} VALUES (DEFAULT,{','.join(['%s' for _ in values])})", values)
        self.connection.commit()

    def fetch_all(self, table):
        self.cursor.execute(f'SELECT * FROM {table} ORDER BY ID;')
        return self.cursor.fetchall()

    def fetch_cat(self, table):
        self.cursor.execute(f"SELECT * FROM {table} WHERE category='IT';")
        return self.cursor.fetchall()

    def delete(self, table, id):
        self.cursor.execute(f"DELETE from {table} WHERE id={id}")
        self.connection.commit()

    def update(self, table, key, value, id):
        print(table, key, value, id)
        print(f"UPDATE {table} SET {key}={value} WHERE id={id}")
        self.cursor.execute(f"UPDATE {table} SET {key}={value} WHERE id={id}")
        self.connection.commit()

    def fetch_distinct(self, table, column):
        self.cursor.execute(
            f'SELECT DISTINCT {column} FROM {table};')
        return self.cursor.fetchall()


