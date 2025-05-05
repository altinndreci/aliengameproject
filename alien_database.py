import sqlite3

class MakeDatabase():
    conn = sqlite3.connect("alien_game.db")
    cursor = conn.cursor()

    #creates table in database for users
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        name TEXT PRIMARY KEY,
        blood INTEGER,
        consequence INTEGER
    );
    """)

    users=[("Joe",100,0)]
    conn.commit

    #creates table in database for items
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS items (
        name TEXT PRIMARY KEY,
        blood_price INTEGER,
        quantity INTEGER
    );
    """)
    #creates table in database for transactions
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        user_name TEXT,
        item_name TEXT,
        steal_time REAL,
        PRIMARY KEY (user_name, item_name),
        FOREIGN KEY (user_name) REFERENCES users(name),
        FOREIGN KEY (item_name) REFERENCES items(name)
    );
    """)

    conn.commit()
    conn.close()