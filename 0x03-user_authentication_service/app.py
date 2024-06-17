#!/usr/bin/env python3
'''flask app'''

from flask import Flask, jsonify, request, abort, make_response
from auth import Auth

AUTH = Auth()
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    '''return the root page'''
    return jsonify({"message": "Bienvenue"})

@app.route('/users', methods=['POST'])
def users():
    '''register a user'''
    email = request.form['email']
    password = request.form['password']
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    
@app.route('/sessions', methods=['POST'])
def sessions():
    '''creates a user session'''
    email = request.form['email']
    password = request.form['password']
    if not AUTH.valid_login(email, password):
        abort(401)
    else:
        session_id = AUTH.create_session(email)
        resp = make_response(jsonify({"email": email, "message": "logged in"}))
        resp.set_cookie('session_id', session_id)
        return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")