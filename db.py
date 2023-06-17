import sqlite3

class Database:
    def __init__(self, db_file):#инициализируем
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
    def add(self, id, token_symbol):#добавляем в табличку
        with self.connection:
            return self.connection.execute("INSERT INTO ARB ('id', 'TOKEN_SYMBOL') VALUES (?, ?)", (id, token_symbol))
    def add_asks_bids(self, token, asks_bids):
        with self.connection:
            return self.connection.execute("UPDATE ARB SET orders = ? WHERE TOKEN_SYMBOL = ?", (asks_bids, token))
    def examintation(self, token_symbol): #есть ли в таблице
        with self.connection:
            res = self.cursor.execute("SELECT * FROM ARB WHERE TOKEN_SYMBOL = ?", (token_symbol,)).fetchall()
            return bool(len(res))
    def delete_alldata_from_table(self):
        with self.connection:
            return self.connection.execute("DELETE FROM ARB")