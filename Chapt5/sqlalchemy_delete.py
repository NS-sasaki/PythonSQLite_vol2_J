from sqlalchemy import delete
from sqlalchemy_settings import engine
from sqlalchemy_tables import authors

# authorsテーブルに対する削除ステートメントを作成
delete_stmt = delete(authors).where(authors.c.name == "Jane Smith")

# ステートメントを実行
with engine.connect() as connection:
    connection.execute(delete_stmt)
    connection.commit()
