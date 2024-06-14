from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    name = ' <script>alert("You have been hacked!");</script>'
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run()
