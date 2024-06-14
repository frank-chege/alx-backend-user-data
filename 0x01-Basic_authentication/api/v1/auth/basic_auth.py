#!/usr/bin/env python3
'''create basic auth class'''

from .auth import Auth
from models.user import User
import re
import base64

class BasicAuth(Auth):
    '''basic auth'''
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        '''returns the base64 part of the auth header'''
        if authorization_header is None or (not isinstance(authorization_header, str)):
            return None
        pat = re.compile('Basic(.*)')
        if not pat.match(authorization_header):
            return None
        tokens = authorization_header.split('Basic')
        return tokens[1]
    
    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        '''decodes the base64 string'''
        if base64_authorization_header is None or (not isinstance(base64_authorization_header, str)):
            return None
        try:
            decoded_str = base64.b64decode(base64_authorization_header)
        except:
            None
        return decoded_str.decode('UTF-8')
    
    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        '''extract user credentials from the decoded bs4 string'''
        if decoded_base64_authorization_header is None or (not isinstance(decoded_base64_authorization_header, str)):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        tokens = decoded_base64_authorization_header.split(':')
        credentials = (tokens[0] ,tokens[1])
        return credentials
    
    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        '''returns user instance based on their credentials'''
        if user_email is None or (not isinstance(user_email, str)) or user_pwd is None or (not isinstance(user_pwd, str)):
            return None
        res = User.search({user_email:user_pwd})
        if res is None or (res is False):
            return None
        if not User.is_valid_password(user_pwd):
            return None
        return res