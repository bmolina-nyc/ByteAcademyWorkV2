## Phase 1 Week 2 Weekend Assignment Part 1:

* Complete all of the stub routes in API trader.

* Have your api trader deployed to a server (not the flask development server) by Monday morning

* To get your code onto a server get your project pushed to a github repository and then in your home folder *on the server* run the following commands:
```
# first rename the myproject folder from the DigitalOcean tutorial to a different directory
mv myproject myproject_bak

# clone your work into a directory called 'myproject' (assuming you used the names from the tutorial)

git clone git@github.com:yourusername/yourprojectname myproject

# create the virtual environment in myproject

cd myproject
python3.6 -m venv myprojectenv

# copy wsgi.py and myproject.ini over from the tutorial project

cd ..
cp myproject_bak/wsgi.py myproject_bak/myproject.ini myproject

# edit your wsgi.py app to import the app object that is created in your api trader project

# instead of 'from myproject import app' have:

from flask_app import app

# depending on your project structure this line might be different but you are importing the app object created by app = Flask(__name__) in one of your project files.

# now install what you need for your app to work

sudo apt install sqlite3

source myprojectenv/bin/activate
pip install flask, requests
deactivate

# run your setup.py
python setup.py

# restart nginx
sudo nginx -t
sudo systemctl restart nginx

# open a new terminal (so you are working on your local machine) and try your curl commands with your *server's* ip address. If my IP is 123.45.67.89 and my ttrader user's api key is 010101010101010101, I might execute:

curl http://123.45.67.89/api/010101010101010101/balance

# and get
{"username": "myuser", "balance": 3.50}

# note that you are not using port 5000. this command might be different if your api is structured to use different routes.
```

Have the API serving all terminal trader features and deployed to a server by your lecture on day 1 of week 2 of phase 2 (probably next monday)
