import pandas as pd
import sqlite3

# 追加するデータを含むDataFrameを作成
new_data = {
    'id': [6, 7],
    'name': ['Frank', 'Grace'],
    'age': [40, 29],
    'city': ['Seattle', 'Boston']
}
df_new = pd.DataFrame(new_data)

# SQLiteデータベースに接続
conn = sqlite3.connect('example.db')

# DataFrameのデータをdata_tableテーブルに追加
df_new.to_sql('data_table', conn, if_exists='append', index=False)

# 接続を閉じる
conn.close()