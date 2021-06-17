from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/Hello")
def hello2():
    return "Hello2 again, Universal!"


if __name__ == '__main__':
    api.run()
