import sqlite3
# データベース接続
conn = sqlite3.connect('inventory_database.db')
# 外部キー制約を有効化
conn.execute("PRAGMA FOREIGN_KEYS = 1")
cursor = conn.cursor()

# 存在しないSupplierIDを持つProductレコードを挿入してみる
try:
    cursor.execute("INSERT INTO Products (ProductName, SupplierID) VALUES (?, ?)", ('Test Product', 9999))
    conn.commit()
except sqlite3.IntegrityError as e:
    print(f"Error: {e}")

conn.close()
