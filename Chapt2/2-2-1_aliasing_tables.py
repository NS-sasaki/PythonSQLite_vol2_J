import sqlite3

# SQLiteデータベースに接続
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# テーブルエイリアスを使用してクエリを実行
cursor.execute("""
SELECT c.CustomerName, o.OrderID 
FROM customers AS c, orders AS o 
WHERE c.CustomerID = o.CustomerID;
""")

# 結果を取得してprintで表示
for row in cursor.fetchall():
    print(row)

# データベース接続を閉じる
conn.close()


# Close the database connection
conn.close()
