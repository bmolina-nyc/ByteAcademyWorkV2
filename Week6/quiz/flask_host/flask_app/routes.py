from flask import redirect, url_for
from flask_app import app

@app.route('/')
def main():
    return redirect(url_for('static', filename='index.html'))

