from sqlalchemy import select
from sqlalchemy_settings import engine
from sqlalchemy_tables import authors, books

# select文とjoinを定義
join_stmt = select(books.c.title, authors.c.name).join(authors, books.c.author_id == authors.c.id)

# ステートメントを実行
with engine.connect() as connection:
    result = connection.execute(join_stmt)
    for row in result:
        print(row)
