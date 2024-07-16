import sqlite3

def insert_data(records):
    conn = sqlite3.connect('transaction_demo.db')
    cursor = conn.cursor()

    try:
        # トランザクションを明示的に開始
        conn.execute("BEGIN")  
        for record in records:
            cursor.execute("INSERT INTO stocks VALUES (?, ?, ?, ?, ?)", record)
        # すべてのステートメントが正常に実行された場合に変更をコミット
        conn.commit()  
        print("レコードが挿入されました")
    except sqlite3.Error as error:
        print("レコードの挿入に失敗しました", error)
        # エラーが発生した場合は変更をロールバック
        conn.rollback()  
    finally:
        conn.close()

# 例として使用するレコードの設定
records_to_insert = [
    ('2021-01-05', 'BUY', 'AAPL', 100, 35.14),
    ('2021-03-28', 'BUY', 'GOOG', 40, 613.3)
]

insert_data(records_to_insert)