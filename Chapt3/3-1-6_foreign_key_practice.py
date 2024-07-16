import sqlite3

# データベースに接続
conn = sqlite3.connect('foreign_key_database.db')
# 外部キー制約を有効化
conn.execute("PRAGMA FOREIGN_KEYS = 1")
cursor = conn.cursor()

# Usersテーブルにデータを挿入
cursor.execute('''
INSERT INTO Users (Username) VALUES ('大谷');
''')

# 正しく挿入されたか確認
cursor.execute('SELECT * FROM Users')
print("Usersテーブルのデータ:")
for row in cursor.fetchall():
    print(row)

# Ordersテーブルにデータを挿入（外部キー制約が成立するケース）
cursor.execute('''
INSERT INTO Orders (OrderDate, UserID) VALUES ('2024-05-18', 1);
''')

# Ordersテーブルにデータを挿入（外部キー制約が成立しないケース）
try:
    cursor.execute('''
    INSERT INTO Orders (OrderDate, UserID) VALUES ('2024-05-18', 2);
    ''')
except sqlite3.IntegrityError as e:
    print(f"外部キー制約違反: {e}")

# 正しく挿入されたか確認
cursor.execute('SELECT * FROM Orders')
print("Ordersテーブルのデータ:")
for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()

print("外部キー制約の動作確認が完了しました")
