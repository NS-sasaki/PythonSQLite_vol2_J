import sqlite3

conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()

# Usersテーブルを作成。UsernameとEmailはNOT NULL設定
cursor.execute('''
CREATE TABLE Users(
    UserID INTEGER PRIMARY KEY,
    Username TEXT NOT NULL,
    Email TEXT NOT NULL
);
''')

conn.commit()
conn.close()

print("NOT NULL制約が設定されたテーブルが作成されました")