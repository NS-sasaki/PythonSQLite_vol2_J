import sqlite3

# SQLiteデータベースへの新しい接続を確立
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# JOIN操作でエイリアスを使用
cursor.execute("""
SELECT o.OrderID, c.CustomerName 
FROM Orders AS o 
INNER JOIN Customers AS c ON o.CustomerID = c.CustomerID;
""")

# エイリアス付きの結合結果を取得してprintで表示
join_results = cursor.fetchall()
for join_result in join_results:
    print(join_result)

# データベース接続を閉じる
conn.close()
