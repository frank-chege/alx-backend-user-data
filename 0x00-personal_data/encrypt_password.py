#!/usr/bin/env python3
'''encrypts a password'''

import bcrypt

def hash_password(password: str)->bytes:
    '''encrypts a password'''
    pwd_bytes = password.encode('UTF-8')
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(pwd_bytes, salt)
    return hashed_pwd

def is_valid(hashed_password: bytes, password: str)->bool:
    '''checks is a password is valid'''
    hash_pwd = password.encode('UTF-8')
    return bcrypt.checkpw(hash_pwd, hashed_password) 