import sqlite3

# データベースに接続する関数を定義
def connect_db():
    return sqlite3.connect('example.db')

# クエリを実行する関数を定義
def execute_query(query, params=()):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

# 一つのレコードを取得する関数を定義
def fetch_one(query, params=()):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, params)
    record = cursor.fetchone()
    conn.close()
    return record

# レコードを作成する関数を定義
def create_record(email, username):
    try:
        execute_query("INSERT INTO users (email, username) VALUES (?, ?)", (email, username))
        return True
    except sqlite3.IntegrityError:
        return False

# レコードを読み取る関数を定義
def read_record_by_email(email):
    return fetch_one("SELECT * FROM users WHERE email=?", (email,))

# レコードを更新する関数を定義
def update_record(email, username):
    if read_record_by_email(email):
        execute_query("UPDATE users SET username=? WHERE email=?", (username, email))
        return True
    return False

# レコードを削除する関数を定義
def delete_record(email):
    execute_query("DELETE FROM users WHERE email=?", (email,))