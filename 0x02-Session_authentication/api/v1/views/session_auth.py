#!/usr/bin/env python3
'''handles all routes for user authentication'''

from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
import importlib
from flask import make_response
from os import getenv

@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_auth():
    '''session auth'''
    email = request.form.get('email')
    pwd = request.form.get('password')
    if email is None or len(email) == 0:
        return jsonify({ "error": "email missing" }), 400
    if pwd is None or len(pwd) == 0:
        return jsonify({ "password": "password missing" }), 400
    user = User.search({email: email})
    if user is None:
        return jsonify({ "error: no user found for this email" }), 404
    if not User.is_valid_password(pwd):
        return jsonify({ "error": "wrong password" }), 401
    from api.v1.app import auth
    auth.create_session(user.id)
    resp =  make_response(User.to_json(user))
    resp.set_cookie(getenv('SESSION_NAME'), user)
    return resp
    