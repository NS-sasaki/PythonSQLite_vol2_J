import sqlite3

# データベースに接続
conn = sqlite3.connect('inventory_database.db')
# 外部キー制約を有効化
conn.execute("PRAGMA FOREIGN_KEYS = 1")
cursor = conn.cursor()

# Suppliersテーブルを作成
cursor.execute('''
CREATE TABLE Suppliers(
    SupplierID INTEGER PRIMARY KEY,
    SupplierName TEXT NOT NULL
);
''')

# 外部キー制約を持つProductsテーブルを作成
cursor.execute('''
CREATE TABLE Products(
    ProductID INTEGER PRIMARY KEY,
    ProductName TEXT NOT NULL,
    SupplierID INTEGER,
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
);
''')

conn.commit()
conn.close()

print("SuppliersテーブルとProductsテーブルが作成されました")
