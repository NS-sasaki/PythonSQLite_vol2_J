from sqlalchemy import insert
from sns_settings import engine
from sns_tables import users, posts, follows

# usersテーブルにデータを挿入
users_data = [
    {"username": "alice", "email": "alice@example.com"},
    {"username": "bob", "email": "bob@example.com"},
    {"username": "charlie", "email": "charlie@example.com"}
]

# postsテーブルにデータを挿入
posts_data = [
    {"user_id": 1, "content": "Hello, world!"},
    {"user_id": 2, "content": "Good morning!"},
    {"user_id": 1, "content": "How's it going?"},
    {"user_id": 3, "content": "Nice to meet you all!"}
]

# followsテーブルにデータを挿入
follows_data = [
    {"follower_id": 1, "followed_id": 2},
    {"follower_id": 2, "followed_id": 3},
    {"follower_id": 3, "followed_id": 1}
]

# データベースへの接続を開き、データを挿入
with engine.connect() as connection:
    # usersテーブルにデータを挿入
    connection.execute(insert(users), users_data)
    # tweetsテーブルにデータを挿入
    connection.execute(insert(posts), posts_data)
    # followsテーブルにデータを挿入
    connection.execute(insert(follows), follows_data)
    # 挿入操作をコミット（確定）
    connection.commit()