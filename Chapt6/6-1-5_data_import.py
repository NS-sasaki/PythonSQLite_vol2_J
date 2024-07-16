import pandas as pd
import sqlite3

# SQLiteデータベースに接続
conn = sqlite3.connect('example.db')

# 仮のテーブル 'data_table' からすべてを選択するSQLクエリの例
query = "SELECT * FROM data_table"

# Pandasを使用してクエリを実行し、結果セットをDataFrameに読み込む
df = pd.read_sql_query(query, conn)

# DataFrameの最初の行を表示
print(df.head(3))