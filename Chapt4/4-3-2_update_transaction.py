import sqlite3

def update_data(updates):
    conn = sqlite3.connect('transaction_demo.db')
    cursor = conn.cursor()

    try:
        # トランザクションを明示的に開始
        conn.execute("BEGIN")        
        # UPDATEステートメントを実行してレコードを更新
        for update in updates:
            cursor.execute("UPDATE stocks SET {} = ? WHERE symbol = ?".format(update['column']), (update['value'], update['symbol']))
        
        # すべてのステートメントが正常に実行された場合に変更をコミット
        conn.commit()
        print("レコードが更新されました")
    except sqlite3.Error as error:
        # エラーが発生した場合、トランザクションをロールバック
        print("レコードの更新に失敗しました", error)
        conn.rollback()
    finally:
        # データベース接続のクローズ
        conn.close()

# 例として使用するレコードの設定
updates_to_make = [
    {'column': 'price', 'value': 600, 'symbol': 'GOOG'},
    {'column': 'qty', 'value': 80, 'symbol': 'AAPL'}
]

update_data(updates_to_make)