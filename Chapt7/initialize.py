import sqlite3

# データベースをセットアップする関数を定義
def setup_database():
    # データベースに接続（存在しない場合は新規作成）
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    # usersテーブルを作成
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            email TEXT PRIMARY KEY,
            username TEXT NOT NULL
        )
    ''')
    # 変更のコミットと接続の終了
    conn.commit()
    conn.close()

# 関数を呼び出してデータベースをセットアップ
setup_database()