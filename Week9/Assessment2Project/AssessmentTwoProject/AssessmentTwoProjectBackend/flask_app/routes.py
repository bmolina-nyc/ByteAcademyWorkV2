from flask import jsonify, abort, request
from flask_app import app
from requests.exceptions import ConnectionError
from app.branch import Branch
from app.employee import Employee
from app.orm import ORM

UNAUTHORIZED = {"error": "unauthorized", "status_code": 401}
NOT_FOUND = {"error": "not found", "status_code": 404}
APP_ERROR = {"error": "application error", "status_code": 500}
BAD_REQUEST = {"error": "bad request", "status_code": 400}

@app.route('/home', methods=['GET'])
def home():
    return jsonify({"test": "this is a test"})

#add/remove/update employees
#create/dete/update branches


@app.route('/branches', methods=['GET'])
def branches():
    branches_list = []
    branches = Branch.all()
    for branch in branches:
        single_branch = {
            "branchName": branch.branchName,
            "branch_pk": branch.pk,
            "city": branch.city,
            "state": branch.state,
            "zip": branch.zip
        }
        branches_list.append(single_branch)

    return jsonify({"branches": branches_list })

@app.route('/employees', methods=['GET'])
def employees():
    employees_list = []
    employees = Employee.all()
    for employee in employees:
        single_employee = {
            "branches_pk": employee.branches_pk,
            "employee_pk": employee.pk,
            "fName": employee.fName,
            "lName": employee.lName,
            "title": employee.title,
            "dob": employee.dob
        }
        employees_list.append(single_employee)

    return jsonify({"employees": employees_list })


@app.route('/employee/<id>')
def employee(id):
    employee = Employee.one_from_pk(id)
    one_employee = []
    json = {
    "branches_pk": employee.branches_pk, 
    "fName": employee.fName, 
    "lName": employee.lName, 
    "title": employee.title,
     "dob": employee.dob,
     "id": id 
     }
    one_employee.append(json)
    return jsonify({"employee": one_employee})


@app.route('/addemployees', methods=['POST'])
def addemployees():
    employee = Employee(fName= request.json['fName'], lName= request.json['lName'], title= request.json['title'], dob= request.json['dob'], branches_pk = request.json['branches_pk'])
    employee.save()
    return jsonify({"branches_pk": employee.branches_pk, "fName": employee.fName, "lName": employee.lName, "title": employee.title, "dob": employee.dob})

@app.route('/updateemployee/<id>', methods=['PUT'])
def updateemployee(id):
    employee = Employee.select_one_where("WHERE pk = ?",(id))
    employee.fName = request.json['fName']
    employee.lName = request.json['lName']
    employee.title = request.json['title']
    employee.dob = request.json['dob']
    employee.branches_pk = request.json['branches_pk']
    employee.save()

    return jsonify({"Message": "Employee Updated"})


@app.route('/deleteemployee/<id>', methods=['PUT'])
def deleteemployee(id):
        employee = Employee.select_one_where("WHERE pk = ?",(id))
        employee.delete()
        
        return jsonify({"Message": "Employee deleted"})

# branches
@app.route('/branch/<id>',)
def branch(id):
    branch = Branch.one_from_pk(id)
    one_branch = []
    json = {
    "branchName": branch.branchName, 
    "city": branch.city, 
    "state": branch.state,
     "zip": branch.zip,
     "id": id 
     }
    one_branch.append(json)
    return jsonify({"branch": one_branch})

@app.route('/addbranch', methods=['POST'])
def addbranch():
    branch = Branch(branchName= request.json['branchName'], city= request.json['city'], state= request.json['state'], zip= request.json['zip'])
    branch.save()
    return jsonify({"branchName": branch.branchName, "city": branch.city, "state": branch.state, "zip": branch.zip})


@app.route('/updatebranch/<id>', methods=['PUT'])
def updatebranch(id):
    branch = Branch.select_one_where("WHERE pk = ?",(id))
    branch.branchName = request.json['branchName']
    branch.city = request.json['city']
    branch.state = request.json['state']
    branch.zip = request.json['zip']
    branch.save()

    return jsonify({"Message": "Branch Updated"})


@app.route('/deletebranch/<id>', methods=['PUT'])
def deletebranch(id):
    branch = Branch.select_one_where("WHERE pk = ?",(id))
    branch.delete()
    
    return jsonify({"Message": "Branch deleted"})






# @app.errorhandler(404)
# def error404():
#     return jsonify({"error": "404 not found"}), 404 

# @app.errorhandler(500) 
# def error500():
#     return jsonify({"error": "application error"}), 500

# @app.route('/api/getkey', methods=['POST'])
# def getkey():
#     if not request.json or 'username' not in request.json or 'password' not in request.json:
#         return jsonify(BAD_REQUEST), 401
#     account = Account.login(request.json['username'], request.json['password'])
#     if not account:
#         return jsonify(UNAUTHORIZED), 401
#     rdict = {'api_key': account.api_key, 'username':account.username}
#     print(rdict)
#     return jsonify(rdict)

# #works
# @app.route('/api/price/<ticker>', methods=['GET'])
# def lookup(ticker):
#     response = get_price(ticker)
#     if response:
#         return jsonify({"symbol": response[0], "price": response[1]})
#     else:
#         return jsonify({"error": "404 not found"}), 404 

# #works
# @app.route('/api/<api_key>/positions', methods=['GET'])
# def positions(api_key):
#     account = Account.authenticate_api(api_key)
#     if not account:
#         return jsonify({"error": "authentication error"}), 401
#     positions = account.get_positions_json()
#     return jsonify({"positions": positions})


# @app.route('/api/<api_key>/position/<ticker>', methods=['GET'])
# def position(api_key, ticker):
#     account = Account.authenticate_api(api_key)
#     if not account:
#         return jsonify({"error": "authentication error"}), 401
#     positions = account.get_positions()
#     for posish in positions:
#         if posish.ticker == ticker:
#             return jsonify({"position": posish.ticker, "shares": posish.shares})
#     return jsonify({"error": "404 not found"}), 404 
  

# @app.route('/api/<api_key>/trades/<ticker>', methods=['GET'])
# def trades(api_key, ticker):
#     account = Account.authenticate_api(api_key)
#     if not account:
#             return jsonify({"error": "authentication error"}), 401
#     ticker_trades = account.get_trades_by_ticker_json(ticker)
#     return jsonify({"trades": ticker_trades})
    
# @app.route('/api/<api_key>/alltrades', methods=['GET'])
# def alltrades(api_key):
#     account = Account.authenticate_api(api_key)
#     if not account:
#         return jsonify({"error": "authentication error"}), 401
#     else:
#         all_trades = account.get_all_trades_json()
#         return jsonify({"trades": all_trades})


# @app.route('/api/<api_key>/balance', methods=['GET'])
# def balance(api_key):
#     account = Account.authenticate_api(api_key)
#     if not account:
#         return jsonify({"error": "authentication error"}), 401
#     return jsonify({"username": account.username, "balance": account.balance})

# @app.route('/api/<api_key>/deposit', methods=['PUT'])
# def deposit(api_key):
#     account = Account.authenticate_api(api_key)
#     if not account:
#         return jsonify({"error": "authentication error"}), 401
#     if not request.json:
#         return jsonify({"error": "bad request"}), 400
#     try:
#         amount = request.json['amount']
#         if amount < 0.0:
#             raise ValueError
#         account.balance += amount
#     except (ValueError, KeyError):
#         return jsonify({"error": "bad reuqest"}), 400
#     account.save()
#     return jsonify({"username": account.username, "balance": account.balance})

# @app.route('/api/<api_key>/buy/<ticker>/<amount>', methods=['POST'])
# def buy(api_key, ticker, amount):
#     account = Account.authenticate_api(api_key)
#     price = get_price(ticker)[1]
#     purchase = int(amount) * int(price)
#     if not account:
#         return jsonify({"error": "authentication error"}), 401
#     if not price:
#         return jsonify({ "error": "bad ticker data"})
#     if not request.json:
#         return jsonify({"error": "bad request"}), 400
#     try:
#         if request.json['amount'] and request.json['ticker']:
#             if account.balance > purchase:
#                 account.buy(ticker, int(amount), int(price), purchase)
#     except (ValueError, KeyError):
#         return jsonify({"error": "bad request"}), 400
#     return jsonify({"username": account.username, "balance": account.balance})


# @app.route('/api/<api_key>/sell/<ticker>/<amount>', methods=['POST'])
# def sell(api_key, ticker, amount):
#     account = Account.authenticate_api(api_key) 
#     position = account.get_position_for(ticker)
#     # ticker, ticker_price = get_price(ticker)[0], get_price(ticker)[1]  
#     # cash = integer(ticker_price) * amount 
#     if not account:
#         return jsonify({"error": "authentication error"}), 401
#     if not ticker:
#         return jsonify({ "error": "bad ticker data"})
#     if not request.json:
#         return jsonify({"error": "bad request"}), 400
#     try:
#         if request.json['amount'] and request.json['ticker']:
#             if position.shares > int(amount):
#                 account.sell(ticker, amount)
#     except (ValueError, KeyError):
#         return jsonify({"error": "bad request"}), 400
#     return jsonify({"username": account.username, "balance": account.balance})
            
# @app.route('/api/accounts', methods=['GET'])
# def accounts():
#     accounts_dic = {}
#     accounts = Account.all()
#     for account in accounts:
#         accounts_dic[account.username] = {
#             "username": account.username,
#             "balance": account.balance,
#             "api-key": account.api_key
#         }
#     return jsonify({"accounts": accounts_dic})

# @app.route('/api/testing', methods=['GET'])
# def testing(): 
#     accounts_dic = {}
#     accounts = Account.all()
#     for account in accounts:
#         accounts_dic[account.username] = {
#             # "username": account.username,
#             "balance": account.balance,
#             "api-key": account.api_key
#         }
#     return jsonify({"accounts": accounts_dic})