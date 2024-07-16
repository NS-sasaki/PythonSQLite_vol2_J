from sqlalchemy import update
from sqlalchemy_settings import engine
from sqlalchemy_tables import authors

# authorsテーブルに対する更新ステートメントを作成
update_stmt = update(authors).where(authors.c.name == "John Smith").values(name="Jane Smith")

# データベースへの接続を開き、更新を実行
with engine.connect() as connection:
    connection.execute(update_stmt)
    connection.commit()