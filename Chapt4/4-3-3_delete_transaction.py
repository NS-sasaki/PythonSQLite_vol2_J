import sqlite3

def delete_data(symbol):
    conn = sqlite3.connect('transaction_demo.db')
    cursor = conn.cursor()

    try:
        # トランザクションを開始
        conn.execute("BEGIN")        
        # DELETEステートメントを実行してレコードを削除
        cursor.execute("DELETE FROM stocks WHERE symbol = ?", (symbol,))
        # DELETE操作が成功した場合、トランザクションをコミット
        conn.commit()
        print("レコードの削除に成功しました")
    except sqlite3.Error as error:
        # エラーが発生した場合、トランザクションをロールバック
        print("レコードの削除に失敗しました", error)
        conn.rollback()
    finally:
        # データベース接続をクローズ
        conn.close()

# 例として使用するシンボルの定義
symbol_to_delete = 'AAPL'

delete_data(symbol_to_delete)