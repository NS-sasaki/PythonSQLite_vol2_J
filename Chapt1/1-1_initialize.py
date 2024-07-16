import sqlite3

# images.dbという名前のデータベースに接続。存在しなければ新しく作成。
conn = sqlite3.connect('images.db')
cursor = conn.cursor()

# imagefilesテーブルの作成。
sql = '''
CREATE TABLE IF NOT EXISTS imagefiles(    
    filename TEXT PRIMARY KEY,        
    imagefile BLOB
)'''
cursor.execute(sql)
conn.commit()

# 作業が終わったら、カーソルとコネクションを閉じて安全に終了。
cursor.close()
conn.close()