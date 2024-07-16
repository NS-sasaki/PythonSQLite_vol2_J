from sqlalchemy import select
from sns_settings import engine
from sns_tables import follows

# select文を定義してuser_id=2がフォローしているuser_idを取得
select_stmt = select(follows.c.followed_id).where(follows.c.follower_id == 2)

# データベースへの接続を開き、クエリを実行
with engine.connect() as connection:
    result = connection.execute(select_stmt)
    for row in result:
        print(f"user_id=2 is following user_id={row.followed_id}")
