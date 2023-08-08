import sqlite3


class Database():
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def create_table(self, sql: str):
        self.cursor.execute(sql)
        self.connection.commit()

    def insert(self, table, *values):
        self.cursor.execute(f"INSERT INTO {table} VALUES ({','.join(['?' for _ in values])})", values)
        self.connection.commit()

    def fetch_all(self, table, **conditions):

        values = conditions.values()

        return self.cursor.execute(
            f"SELECT * FROM {table} WHERE {' and '.join([f'{condition}=?' for condition in conditions])}",
            tuple(values)
            )

    def delete(self, table, id):
        self.cursor.execute(f"DELETE from {table} WHERE id={id}")
        self.connection.commit()

    def update(self, table, key, value, id):
        print(table, key, value, id)
        print(f"UPDATE {table} SET {key}={value} WHERE id={id}")
        self.cursor.execute(f"UPDATE {table} SET {key}={value} WHERE id={id}")
        self.connection.commit()
