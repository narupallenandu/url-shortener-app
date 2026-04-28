from flask import Flask, request, redirect, render_template
import sqlite3
import string
import random

app = Flask(__name__)

# Initialize DB
def init_db():
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            short TEXT UNIQUE,
            original TEXT,
            clicks INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Generate short code
def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

@app.route('/', methods=['GET', 'POST'])
def home():
    short_url = None

    if request.method == 'POST':
        original_url = request.form['url']

        conn = sqlite3.connect('urls.db')
        c = conn.cursor()

        # Check if URL already exists
        c.execute("SELECT short FROM urls WHERE original=?", (original_url,))
        existing = c.fetchone()

        if existing:
            short_code = existing[0]
        else:
            short_code = generate_short_code()
            c.execute("INSERT INTO urls (short, original) VALUES (?, ?)", (short_code, original_url))
            conn.commit()

        conn.close()

        short_url = request.host_url + short_code

    return render_template('index.html', short_url=short_url)

@app.route('/<code>')
def redirect_url(code):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()

    c.execute("SELECT original, clicks FROM urls WHERE short=?", (code,))
    result = c.fetchone()

    if result:
        original_url, clicks = result
        c.execute("UPDATE urls SET clicks=? WHERE short=?", (clicks + 1, code))
        conn.commit()
        conn.close()
        return redirect(original_url)

    conn.close()
    return "URL not found"

@app.route('/stats')
def stats():
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()

    c.execute("SELECT short, original, clicks FROM urls")
    data = c.fetchall()

    conn.close()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)