#!/usr/bin/env python3
'''encrypts a password'''

import bcrypt

def hash_password(password: str)->bytes:
    '''encrypts a password'''
    pwd_bytes = password.encode('UTF-8')
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(pwd_bytes, salt)
    return hashed_pwd