import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users
                     (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS clients
                     (id TEXT PRIMARY KEY, name TEXT, mobile TEST, descript TEXT)''')


with sqlite3.connect('my_database.db') as conn:
    cursor = conn.cursor()
    sql = "INSERT INTO users (name, age) VALUES (?,?)"
    data = ("Bob", 25)
    cursor.execute(sql, data)
    conn.commit()
print("Database is successful.")
conn.close()