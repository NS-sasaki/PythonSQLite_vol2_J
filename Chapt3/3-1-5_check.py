import sqlite3

conn = sqlite3.connect('check_constraint_database.db')
cursor = conn.cursor()

# # ユーザー年齢 > 18 のチェック制約を設定したテーブルを作成
cursor.execute('''
CREATE TABLE Users(
    UserID INTEGER PRIMARY KEY,
    Username TEXT NOT NULL,
    Age INTEGER CHECK(Age > 18)
);
''')

conn.commit()
conn.close()

print("年齢にチェック制約を持つテーブルが作成されました")
