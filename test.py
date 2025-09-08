import sqlite3

conn = sqlite3.connect("messages.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM messages")

rows = cursor.fetchall()
for row in rows:
    print(f"ID: {row[0]},\n Name: {row[1]},\n Email: {row[2]},\n Message: {row[3]}")

conn.close()
