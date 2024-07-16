import sqlite3

# 'example.db'という名前のSQLiteデータベースに接続
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# INNER JOINを実行するためのSQLコマンド
cursor.execute("""
SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;
""")

# 一致するレコードを取得して表示
orders_with_customers = cursor.fetchall()
for order in orders_with_customers:
    print(order)

# 接続を閉じる
conn.close()