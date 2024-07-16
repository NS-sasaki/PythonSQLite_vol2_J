from my_functions import open_images_db, close_database

# データベースを開く
conn, cursor = open_images_db()

# データベースから特定の画像ファイルを取得するためのパラメータを設定
params = ['0.png']

# 画像ファイルのデータを取得するSQLクエリを実行
sql = '''SELECT imagefile FROM imagefiles WHERE filename=?'''
cursor.execute(sql, params)

# 取得した画像ファイルのデータを格納
image_file = cursor.fetchone()

# 新しい画像ファイル名を設定
file_name = 'newimage.png'

# バイナリーモードで新しい画像ファイルを開き、データベースから取得した画像データを書き込み保存
with open(file_name, 'wb') as f:
    f.write(image_file[0])

# データベースの接続を閉じる
close_database(cursor, conn)
