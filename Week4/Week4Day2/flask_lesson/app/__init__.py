from flask import Flask #this is a python library and web framework

app = Flask(__name__)

from app import routes

