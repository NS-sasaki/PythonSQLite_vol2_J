import sqlite3

# データベースに接続（または新規作成）
conn = sqlite3.connect('inventory_database.db')
# 外部キー制約を有効化
conn.execute("PRAGMA FOREIGN_KEYS = 1")
cursor = conn.cursor()

# Suppliersテーブルにデータを挿入
suppliers_data = [
    (1, 'Tokyo Supplies'),   # 仕入先ID 1、仕入先名 'Tokyo Supplies'
    (2, 'Kyoto Goods'),     # 仕入先ID 2、仕入先名 'Kyoto Goods'
    (3, 'Osaka Equipment')  # 仕入先ID 3、仕入先名 'Osaka Equipment'
]

# データの挿入
cursor.executemany("INSERT INTO Suppliers (SupplierID, SupplierName) VALUES (?, ?)", suppliers_data)

# Productsテーブルにデータを挿入
products_data = [
    (1, 'Laptop', 1),            # 商品ID 1、商品名 'Laptop'、仕入先ID 1
    (2, 'Desktop Computer', 1),  # 商品ID 2、商品名 'Desktop Computer'、仕入先ID 1
    (3, 'Smartphone', 2),        # 商品ID 3、商品名 'Smartphone'、仕入先ID 2
    (4, 'Tablet', 3)             # 商品ID 4、商品名 'Tablet'、仕入先ID 3
]

# データの挿入
cursor.executemany("INSERT INTO Products (ProductID, ProductName, SupplierID) VALUES (?, ?, ?)", products_data)

# 変更をコミットしてデータベース接続を閉じる
conn.commit()
conn.close()
