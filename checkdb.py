import sqlite3
import subprocess
import requests
import json

try:
    conn = sqlite3.connect('adp.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")  # 假设存在一个名为 some_table 的表
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
except sqlite3.Error as e:
    print("Error connecting to database:", e)
    

def search_by_mobile(mobile):
    url = "http://adp.mq-tech.net:5000/reports/search_by_mobile"
    payload = {"mobile": mobile}
    headers = {'Content-Type': 'application/json'}
    
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error calling API:", e)
        return None

# Example usage

