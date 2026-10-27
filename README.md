# SQLi Lab (Educational)

A deliberately vulnerable Flask login form to demonstrate SQL Injection. 

> **WARNING:** This app is INTENTIONALLY INSECURE. Only run on `localhost`/your own isolated lab. Do **not** expose it to the internet.

## Setup (local)

1. Open a terminal in `sqli-lab/`
2. Create and activate a virtual environment

   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the database
   ```bash
   python init_db.py
   ```

5. Run the app
   ```bash
   python app.py
   ```

6. Open [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Demo payloads

| Payload (Username) | Password | Result |
|---|---|---|
| `admin' --` | `anything` | Logs in as admin (password check is commented) |
| `' OR '1'='1' --` | `anything` | Logs in (query becomes always true) |

Look at the "Executed SQL Query" box to see what actually runs.

## How to fix it (correct approach)

Never concatenate user input. Use parameterized queries. For SQLite:

```python
cur.execute("SELECT id, username FROM users WHERE username = ? AND password = ?", (username, password))
```

Also consider: hashing passwords (e.g. `werkzeug.security`), rate limiting, and input validation.

## Free deployment options

- [Render](https://render.com/docs/deploy-flask) - Create a new Web Service, connect repo, set start command `gunicorn app:app`
- [Railway](https://docs.railway.app/guides/flask) - Similar, auto-detects or use `gunicorn app:app`
- [PythonAnywhere](https://help.pythonanywhere.com/pages/Flask/) - Easy for small demos

If deploying, **do not use this vulnerable version**. Only deploy a fixed version if you actually need it online.

## Test users
- `admin` / `supersecret123`
- `test` / `password123`
