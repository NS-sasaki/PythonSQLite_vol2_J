from sqlalchemy import insert
from sqlalchemy_settings import engine
from sqlalchemy_tables import authors, books

# authorsテーブルにデータを挿入
authors_data = [
    {"name": "Jane Smith"},
    {"name": "John Doe"},
    {"name": "Emily Davis"}
]

# booksテーブルにデータを挿入
books_data = [
    {"title": "Python Programming", "author_id": 1},
    {"title": "SQLAlchemy for Beginners", "author_id": 2},
    {"title": "Advanced SQLAlchemy", "author_id": 2},
    {"title": "Data Science with Python", "author_id": 3}
]

# データベースへの接続を開き、データを挿入
with engine.connect() as connection:
    # authorsテーブルにデータを挿入
    for author in authors_data:
        insert_stmt = insert(authors).values(author)
        connection.execute(insert_stmt)

    # booksテーブルにデータを挿入
    for book in books_data:
        insert_stmt = insert(books).values(book)
        connection.execute(insert_stmt)

    # 挿入操作をコミット（確定）
    connection.commit()
