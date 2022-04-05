import sqlite3

connection = sqlite3.connect("blog.sqlite")
cur = connection.cursor()
cur.execute('''CREATE TABLE posts 
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(200) NOT NULL,
            description TEXT NOT NULL,
            date TEXT NOT NULL);''')
connection.close()