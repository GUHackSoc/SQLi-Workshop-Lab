import sqlite3 
import os

DB_PATH = os.path.join("instance", "users.db")
os.makedirs("instance", exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
""")

# Clear old data for repeatable demos
cur.execute("DELETE FROM users")

# Seed a known user
cur.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ("admin", "supersecret123"))
cur.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ("test", "password123"))

conn.commit()
conn.close()

print(f"[+] Database initialized at {DB_PATH}")
print("[+] Users created: admin / test")
