import requests
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

def get_chart(ticker):
    result = requests.get('https://api.iextrading/1.0/stock/{}/chart'.format(ticker))
    if result.status_code == 200:
      return result.json
    return {}

@app.route('/chart/<ticker>')
def chart(ticker):
    return jsonify({"ticker": ticker})

@app.route('/chart/<ticker>')
def chart(ticker):
    return jsonify(get_chart(ticker))

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)