import sqlite3

# SQLiteデータベースに接続
conn = sqlite3.connect('example.db')

# カーソルオブジェクトを作成
cursor = conn.cursor()

# data_tableテーブルを作成
cursor.execute('''
    CREATE TABLE data_table (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        city TEXT
    )
''')

# ダミーデータを挿入
data = [
    (1, 'Alice', 30, 'New York'),
    (2, 'Bob', 25, 'Los Angeles'),
    (3, 'Charlie', 35, 'Chicago'),
    (4, 'David', 28, 'Miami'),
    (5, 'Eve', 22, 'San Francisco')
]

cursor.executemany('''
    INSERT INTO data_table (id, name, age, city)
    VALUES (?, ?, ?, ?)
''', data)

conn.commit()
conn.close()