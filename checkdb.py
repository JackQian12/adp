import sqlite3

try:
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")  # 假设存在一个名为 some_table 的表
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
except sqlite3.Error as e:
    print("Error connecting to database:", e)