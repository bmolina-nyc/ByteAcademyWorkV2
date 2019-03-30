#! /usr/bin/env python3

import os
from flask_app import app 
from app.orm import ORM


DIR = os.path.dirname(__file__)
DBFILENAME = "bank.db"
DBPATH = os.path.join(DIR, 'data', DBFILENAME)

if __name__ == "__main__":
    app.run(debug=True)