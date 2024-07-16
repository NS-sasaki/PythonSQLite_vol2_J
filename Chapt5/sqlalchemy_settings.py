from sqlalchemy import create_engine, MetaData

# データベース接続文字列を定義
database_url = 'sqlite:///books.db'

# データベースエンジンを作成
engine = create_engine(database_url)

# MetaDataオブジェクトをインスタンス化
metadata = MetaData()