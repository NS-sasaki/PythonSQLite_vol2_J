from my_functions import open_images_db, close_database

# 画像データを開き、binary_imagedataへ格納
file_path = '0.png'
with open(file_path, 'rb') as f:
    binary_imagedata = f.read()

conn, cursor = open_images_db()
file_name = '0.png'
params = [file_name, binary_imagedata]
sql = '''INSERT INTO imagefiles(filename,imagefile) VALUES(?,?)'''
cursor.execute(sql, params)
conn.commit()
close_database(cursor, conn)
