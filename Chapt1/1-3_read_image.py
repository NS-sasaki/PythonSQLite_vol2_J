from my_functions import open_images_db, close_database
from PIL import Image
from io import BytesIO # メモリ上でバイナリーデータを扱う

# データベースを開く
conn, cursor = open_images_db()

# 取得する画像のファイル名を設定
params = ['0.png']

# SQLクエリの実行
sql = '''SELECT imagefile FROM imagefiles WHERE filename=?'''
cursor.execute(sql, params)

# カーソルからデータを取得
image_file = cursor.fetchone()
print(image_file)

# 画像のバイナリーデータをPillowで開き、画像を表示
img = Image.open(BytesIO(image_file[0]))
img.show()

# データベースを閉じる
close_database(cursor, conn)
