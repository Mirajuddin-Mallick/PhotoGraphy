from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create database & table if not exists
def init_db():
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS messages
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT,
                       email TEXT,
                       message TEXT)''')
    conn.commit()
    conn.close()

# Home page with all messages
@app.route("/")
def index():
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, email, message FROM messages ORDER BY id DESC")
    messages = [{"name": row[0], "email": row[1], "message": row[2]} for row in cursor.fetchall()]
    conn.close()
    return render_template("index.html", messages=messages)

# Handle form submission
@app.route("/send", methods=["POST"])
def send():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (name, email, message) VALUES (?, ?, ?)", (name, email, message))
    conn.commit()
    conn.close()

    return redirect("/")  # Refresh page to show the message

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
