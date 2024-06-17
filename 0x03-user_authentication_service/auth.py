#!/usr/bin/env python3
'''encrypt a password'''

import bcrypt

def _hash_password(password: str)->bytes:
    '''hashes a password'''
    pwd_bytes = password.encode('UTF-8')
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(pwd_bytes, salt)
    return hashed_pwd