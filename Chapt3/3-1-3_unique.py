import sqlite3

conn = sqlite3.connect('unique_user_database.db')
cursor = conn.cursor()

# Eメールアドレスがユニーク制約を設定したUsersテーブルを作成
cursor.execute('''
CREATE TABLE Users(
    UserID INTEGER PRIMARY KEY,
    Username TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE
);
''')

conn.commit()
conn.close()

print("Eメールアドレスにユニーク制約が設定されたUsersテーブルが作成されました。")
