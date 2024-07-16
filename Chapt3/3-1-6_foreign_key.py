import sqlite3

# データベースに接続
conn = sqlite3.connect('foreign_key_database.db')
# 外部キー制約を有効化
conn.execute("PRAGMA FOREIGN_KEYS = 1")
cursor = conn.cursor()

# Usersテーブルを作成
cursor.execute('''
CREATE TABLE Users(
    UserID INTEGER PRIMARY KEY,
    Username TEXT NOT NULL
);
''')

# Usersテーブルと関連するOrderテーブルを作成
cursor.execute('''
CREATE TABLE Orders(
    OrderID INTEGER PRIMARY KEY,
    OrderDate TEXT NOT NULL,
    UserID INTEGER,
    FOREIGN KEY(UserID) REFERENCES Users(UserID)
);
''')

conn.commit()
conn.close()

print("外部キー制約を持つテーブルが作成されました")
