import sqlite3

# images.dbに接続する関数
def open_images_db():
    conn = sqlite3.connect('images.db')
    cursor = conn.cursor()
    return conn, cursor

# データベースの接続を切断する関数
def close_database(cursor, conn):
    cursor.close()
    conn.close()
