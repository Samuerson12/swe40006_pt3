from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
      <head><title>SWE40006 Task 3 - Credit</title></head>
      <body style="font-family:Arial; max-width:600px; margin:80px auto; text-align:center">
        <h1 style="color:#2e74b5">SWE40006 Portfolio Task 3</h1>
        <p>Deployed by Samuel Chang via Render</p>
        <p>Flask Web Service</p>
      </body>
    </html>
    '''

if __name__ == '__main__':
    app.run()
