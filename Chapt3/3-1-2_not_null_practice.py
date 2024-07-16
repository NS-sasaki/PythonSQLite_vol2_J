import sqlite3

# データベース接続を開く
conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()

# NOT NULL制約を持つEmail列に対してNULLを挿入してみる
try:
    cursor.execute("INSERT INTO Users (Username, Email) VALUES (?, ?)", ('NewUser', None))
    conn.commit()
except sqlite3.IntegrityError as e:
    # エラーメッセージを出力
    print(f"Error: {e}")

# データベース接続を閉じる
conn.close()
