import sqlite3

# SQLiteデータベースに接続（存在しない場合は作成）
conn = sqlite3.connect('example.db')
c = conn.cursor()

# 'orders'テーブルを作成
c.execute('''CREATE TABLE IF NOT EXISTS orders
             (OrderID INT PRIMARY KEY     NOT NULL,
              CustomerID INT              NOT NULL,
              ProductName TEXT           NOT NULL);''')

# 'orders'テーブルにデータを挿入
orders_data = [
    (3268, 1, 'yPhone18'),
    (654, 2, 'T-stick'),
    (26, 3, 'S-prime'),
    (885, 4, 'AAD')
]

c.executemany('INSERT INTO orders (OrderID, CustomerID, ProductName) VALUES (?, ?, ?)', orders_data)

# 'customers'テーブルを作成
c.execute('''CREATE TABLE IF NOT EXISTS customers
             (CustomerID INT PRIMARY KEY     NOT NULL,
              CustomerName TEXT              NOT NULL);''')

# 'customers'テーブルにデータを挿入
customers_data = [
    (1, 'Yamashita'),
    (2, 'Takeuchi'),
    (3, 'Smith'),
    (4, 'Arnold')
]

c.executemany('INSERT INTO customers (CustomerID, CustomerName) VALUES (?, ?)', customers_data)

# 変更をコミットして接続を閉じる
conn.commit()
conn.close()