from flask import render_template, jsonify
from app import app

@app.route('/')

def main():
    return render_template("index.html")

@app.route('/saywhat/<what>')
def saywhat(what):
    return render_template("saywhat.html", what=what)

@app.route('/api')
def api():
    data = {"message": "hello world"}
    return jsonify(data)