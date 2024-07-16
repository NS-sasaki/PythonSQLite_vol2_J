import sqlite3

# 'example.db'という名前のSQLiteデータベースに接続
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# CROSS JOINを実行するためのSQLコマンド
cursor.execute("""
SELECT customers.CustomerName, orders.OrderID, orders.ProductName
FROM customers
CROSS JOIN orders;
""")

# すべての可能な組み合わせを取得して表示
all_combinations = cursor.fetchall()
for combination in all_combinations:
    print(combination)

# 接続を閉じる
conn.close()
