from flask import Flask, json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/Hello")
def hello2():
    return "Hello2 again, Universal!"

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

@api.route('/companies', methods=['GET'])
def get_companies():
  return json.dumps(companies)

if __name__ == '__main__':
    api.run()
