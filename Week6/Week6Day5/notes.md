For your recent Terminal Trader API

pip install flask-cors

- Install flask cors in a virtual environment
in your app __init__.py file in flask_app/__init__.py 

from flask_cors import CORS
cors = CORS(app)

post requests with fetch 
prom = fetch('/api/getkey',{
    method = 'POST',
    headers:{
        carters 'accept' and 'content type' code
    }, 
    body: JSON.stringify({'username':'name', 'password': 'user})
})
then promise code then - 