from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "This is my homepage."

@app.route('/hello')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()