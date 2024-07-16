import sqlite3

# データベースに再接続
conn = sqlite3.connect('unique_user_database.db')
cursor = conn.cursor()

# 同じEmailアドレスを持つ2つのレコードを挿入しようとして、UNIQUE制約違反のエラーを発生させる
try:
    # 最初のレコード挿入
    cursor.execute("INSERT INTO Users (Username, Email) VALUES (?, ?)", ('User1', 'user@example.com'))
    conn.commit()
    
    # 同じEmailで2番目のレコードを挿入しようとする
    cursor.execute("INSERT INTO Users (Username, Email) VALUES (?, ?)", ('User2', 'user@example.com'))
    conn.commit()
except sqlite3.IntegrityError as e:
    # UNIQUE制約違反のエラーメッセージを捕捉して出力
    print(f"Error: {e}")

# データベース接続を閉じる
conn.close()
