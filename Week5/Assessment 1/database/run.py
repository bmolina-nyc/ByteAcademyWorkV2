#! /usr/bin/env python3
import os
from app.orm import ORM

DIR = os.path.dirname(__file__)
DBFILENAME = 'campus_students.db'
DBPATH = os.path.join(DIR, 'data', DBFILENAME)

ORM.dbpath = DBPATH