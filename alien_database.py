import sqlite3
from ClassUser import User

#Creating the class for the database
class MakeDatabase():
    def __init__(self, player):
        username = player.get_name()

        conn = sqlite3.connect("alien_game.db")
        cursor = conn.cursor()

        #creates table in database for users
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            blood INTEGER,
            consequence INTEGER
        )
        """)
        users=[(username, 100, 0)]
        cursor.executemany("INSERT OR IGNORE INTO users (username, blood, consequence) VALUES (?, ?, ?)", users)



        #creates table in database for items
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            name TEXT PRIMARY KEY,
            blood_price INTEGER,
            quantity INTEGER
        )
        """)
        #items in the database that can be stolen
        items = [
    ("Alien Gun", 50, 1),
    ("Alien Knife", 30, 1),
    ("Alien Snot", 10, 1),
    ("Bomb Launcher", 60, 1),
    ("Alien Shield", 40, 1),
    ("Alien Potion", 20, 1)]

        cursor.executemany("INSERT OR IGNORE INTO items (name, blood_price, quantity) VALUES (?, ?, ?)", items)
        
        #creates table in database for transactions
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            username TEXT,
            item_name TEXT,
            action TEXT,
            action_time REAL,
            FOREIGN KEY (username) REFERENCES users(username),
            FOREIGN KEY (item_name) REFERENCES items(name)
        );
        """)

        conn.commit()
        conn.close()

