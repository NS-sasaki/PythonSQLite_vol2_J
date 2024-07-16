from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime, Text
from sns_settings import metadata, engine
from datetime import datetime

# usersテーブルを定義
users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('username', String, nullable=False, unique=True),
              Column('email', String, nullable=False, unique=True),
              Column('created_at', DateTime, default=datetime.utcnow)
              )

# postsテーブルを定義
posts = Table('posts', metadata,
               Column('id', Integer, primary_key=True),
               Column('user_id', Integer, ForeignKey('users.id'), nullable=False),
               Column('content', Text, nullable=False),
               Column('created_at', DateTime, default=datetime.utcnow)
               )

# followsテーブルを定義
follows = Table('follows', metadata,
                Column('follower_id', Integer, ForeignKey('users.id'), primary_key=True),
                Column('followed_id', Integer, ForeignKey('users.id'), primary_key=True),
                Column('created_at', DateTime, default=datetime.utcnow)
                )

# データベースにテーブルを作成
metadata.create_all(engine)
