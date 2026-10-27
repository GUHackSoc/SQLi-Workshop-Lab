import os
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
DB_PATH = os.path.join("instance", "users.db")

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    query_shown = None

    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        query = f"SELECT id, username FROM users WHERE username = '{username}' AND password = '{password}'"
        query_shown = query

        try:
            cur.execute(query)
            user = cur.fetchone()
        except Exception as e:
            error = f"SQL Error: {e}"
            user = None
        finally:
            conn.close()

        if user:
            return render_template("login.html", success=f"Logged in as {user[1]} (id={user[0]})", query=query_shown)
        else:
            if not error:
                error = "Invalid username or password."
            return render_template("login.html", error=error, query=query_shown)

    return render_template("login.html")

if __name__ == "__main__":
    # Only for local testing
    app.run(debug=True)
