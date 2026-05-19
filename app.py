import os
from flask import Flask, request
import psycopg2

app = Flask(__name__)

def get_db():
    return psycopg2.connect(os.environ['DATABASE_URL'])

def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id SERIAL PRIMARY KEY,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def home():
    conn = get_db()
    cur = conn.cursor()

    if request.method == 'POST':
        msg = request.form.get('message')
        if msg:
            cur.execute('INSERT INTO messages (message) VALUES (%s)', (msg,))
            conn.commit()

    cur.execute('SELECT message FROM messages ORDER BY id DESC')
    messages = cur.fetchall()
    cur.close()
    conn.close()

    messages_html = ''.join(f'<li>{m[0]}</li>' for m in messages)

    return f'''
    <html>
      <head><title>SWE40006 Task 3 - HD</title></head>
      <body style="font-family:Arial; max-width:600px; margin:80px auto; text-align:center">
        <h1 style="color:#2e74b5">SWE40006 Portfolio Task 3</h1>
        <p>Deployed by Samuel Chang via Render</p>
        <p>PostgreSQL Database </p>
        <form method="POST">
          <input name="message" placeholder="Enter a message" style="padding:8px; width:300px"/>
          <button type="submit" style="padding:8px 16px">Submit</button>
        </form>
        <h3>Messages from Database :</h3>
        <ul style="list-style:none; padding:0">{messages_html}</ul>
      </body>
    </html>
    '''

init_db()

if __name__ == '__main__':
    app.run()
