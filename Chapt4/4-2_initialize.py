import sqlite3

# データベース接続
conn = sqlite3.connect('transaction_demo.db')
cursor = conn.cursor()

# テーブルの作成
cursor.execute('''
CREATE TABLE stocks
(date TEXT, trans TEXT, symbol TEXT, qty REAL, price REAL)
''')
print("データベースとテーブルが作成されました")

# データベース接続のクローズ
conn.close()