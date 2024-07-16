import sqlite3

# データベース接続
conn = sqlite3.connect('inventory_database.db')
# 外部キー制約を有効化
conn.execute("PRAGMA FOREIGN_KEYS = 1")
cursor = conn.cursor()

# JOINクエリの実行
cursor.execute('''
SELECT Products.ProductName, Suppliers.SupplierName
FROM Products
INNER JOIN Suppliers ON Products.SupplierID = Suppliers.SupplierID
''')

#クエリ結果の取得
rows = cursor.fetchall()

# 結果の表示
for row in rows:
    print(f"Product: {row[0]}, Supplier: {row[1]}")

# データベース接続のクローズ
conn.close()
