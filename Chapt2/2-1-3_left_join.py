import sqlite3

# 'example.db'というSQLiteデータベースに再接続
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# LEFT JOINのためのSQLコマンド
cursor.execute("""
SELECT orders.OrderID, orders.CustomerID, orders.ProductName, customers.CustomerName
FROM orders
LEFT JOIN customers ON orders.CustomerID = customers.CustomerID;
""")

# すべての注文と、利用可能な場合は顧客名を取得して表示
all_orders = cursor.fetchall()
for order in all_orders:
    print(order)

# データベース接続を閉じる
conn.close()