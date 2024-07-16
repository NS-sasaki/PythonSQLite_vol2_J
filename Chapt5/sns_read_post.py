from sqlalchemy import select
from sns_settings import engine
from sns_tables import posts

# select文を定義してuser_id=1の投稿を取得
select_stmt = select(posts).where(posts.c.user_id == 1)

# データベースへの接続を開き、クエリを実行
with engine.connect() as connection:
    result = connection.execute(select_stmt)
    for row in result:
        print(f"Post ID: {row.id}, Content: {row.content}, Created At: {row.created_at}")