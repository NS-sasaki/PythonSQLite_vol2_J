from sqlalchemy import insert
from sqlalchemy_settings import engine
from sqlalchemy_tables import authors

# データの挿入
insert_stmt = insert(authors).values(name="John Smith")

# データベースへの接続を開き、挿入を実行
with engine.connect() as connection:
    # SQL文をデータベースに送信し、実行
    connection.execute(insert_stmt)
    # 挿入操作をコミット（確定）
    connection.commit()
