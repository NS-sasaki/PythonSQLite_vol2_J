from sqlalchemy import insert
from sns_settings import engine
from sns_tables import posts

# データの挿入
# 例: ユーザーIDが1のユーザーが投稿する場合
user_id = 1
post_content = "This is a new post by user 1"

# postsテーブルにデータを挿入するためのステートメントを作成
insert_stmt = insert(posts).values(user_id=user_id, content=post_content)

# データベースへの接続を開き、挿入を実行
with engine.connect() as connection:
    connection.execute(insert_stmt)
    connection.commit()
