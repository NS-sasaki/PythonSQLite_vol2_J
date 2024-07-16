import sqlite3

# データベースに再接続
conn = sqlite3.connect('check_constraint_database.db')
cursor = conn.cursor()

# Ageが18以下のレコードを挿入しようとして、CHECK制約違反のエラーを発生させる
try:
    # Ageが18以下のユーザーを挿入しようとする
    cursor.execute("INSERT INTO Users (Username, Age) VALUES (?, ?)", ('YoungUser', 10))
    conn.commit()
except sqlite3.IntegrityError as e:
    # CHECK制約違反のエラーメッセージを捕捉して出力
    print(f"Error: {e}")

# データベース接続を閉じる
conn.close()
