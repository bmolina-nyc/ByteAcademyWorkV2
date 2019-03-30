#! /usr/bin/env python3
import os
from app.orm import ORM

DIR = os.path.dirname(__file__)
DBFILENAME = 'bank.db'
DBPATH = os.path.join(DIR, 'data', DBFILENAME)

# child classes default to ORM'm dbpath if it is not set
ORM.dbpath = DBPATH
