#!/usr/bin/env python3
'''flask app'''

from flask import Flask, jsonify, request
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
        Auth.register_user(email, password)
        return jsonify({f"email": {email}, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")