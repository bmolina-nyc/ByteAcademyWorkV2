from flask import jsonify, request
from flask_app import app
from app import util, Account
from requests.exceptions import ConnectionError

UNAUTHORIZED = {"error": "unauthorized", "status_code": 401}
NOT_FOUND = {"error": "not found", "status_code": 404}
APP_ERROR = {"error": "application error", "status_code": 500}
BAD_REQUEST = {"error": "bad request", "status_code": 400}


@app.errorhandler(404)
def error404(e):
    return jsonify(NOT_FOUND), 404


@app.errorhandler(500)
def error500(e):
    return jsonify(APP_ERROR), 500


@app.route('/')
def root():
    return jsonify({"name": "API Trader"})


@app.route('/api/price/<ticker>')
def price(ticker):
    try:
        price = util.get_price(ticker)
    except ConnectionError:
        return jsonify(NOT_FOUND), 404
    return jsonify({"ticker": ticker, "price": price})


@app.route('/api/<api_key>/balance')
def balance(api_key):
    account = Account.api_authenticate(api_key)
    if not account:
        return jsonify(UNAUTHORIZED), 401
    return jsonify({"username": account.username, "balance": account.balance})


@app.route('/api/<api_key>/positions')
def positions(api_key):
    account = Account.api_authenticate(api_key)
    if not account:
        return jsonify(UNAUTHORIZED), 401
    positions = account.get_positions()
    json_list = [position.json() for position in positions]
    return jsonify({"username": account.username, "positions": json_list})


# TODO:

# position for

# trades

# trades for

@app.route('/api/<api_key>/deposit', methods=['PUT'])
def deposit(api_key):
    print(request.json)
    if not request.json or 'amount' not in request.json:
        return jsonify(BAD_REQUEST), 400
    account = Account.api_authenticate(api_key)
    if not account:
        return jsonify(UNAUTHORIZED), 401
    amount = request.json['amount']
    if not (isinstance(amount, float) or isinstance(amount, int)) or amount < 0:
        return jsonify(BAD_REQUEST), 400
    account.deposit(amount)
    account.save()
    rdict = {"username": account.username, "balance": account.balance}
    print(rdict)
    return jsonify({"username": account.username, "balance": account.balance})


@app.route('/api/getkey', methods=['POST'])
def getkey():
    if not request.json or 'username' not in request.json or 'password' not in request.json:
        return jsonify(BAD_REQUEST), 401
    account = Account.login(request.json['username'], request.json['password'])
    if not account:
        return jsonify(UNAUTHORIZED), 401
    rdict = {'api_key': account.api_key}
    print(rdict)
    return jsonify(rdict)
