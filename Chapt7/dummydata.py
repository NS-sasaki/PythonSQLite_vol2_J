import sqlite3

def insert_dummy_data():
    dummy_data = [
        ('taro@example.com', 'Taro Yamada'),
        ('hanako@example.com', 'Hanako Suzuki'),
        ('ichiro@example.com', 'Ichiro Tanaka'),
        ('sachiko@example.com', 'Sachiko Kato'),
        ('hiroshi@example.com', 'Hiroshi Matsumoto'),
        ('miyuki@example.com', 'Miyuki Saito'),
        ('kenta@example.com', 'Kenta Nakamura'),
        ('akiko@example.com', 'Akiko Kobayashi'),
        ('yusuke@example.com', 'Yusuke Yamamoto'),
        ('emiko@example.com', 'Emiko Ishikawa')
    ]

    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO users (email, username) VALUES (?, ?)', dummy_data)
    conn.commit()
    conn.close()

insert_dummy_data()