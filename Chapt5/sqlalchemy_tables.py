from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy_settings import metadata, engine

# authorsテーブルを定義
authors = Table('authors', metadata,
                Column('id', Integer, primary_key=True),
                Column('name', String)
                )

# booksテーブルを定義
books = Table('books', metadata,
              Column('id', Integer, primary_key=True),
              Column('title', String),
              Column('author_id', Integer, ForeignKey('authors.id'))
              )

# データベースにテーブルを作成
metadata.create_all(engine)
