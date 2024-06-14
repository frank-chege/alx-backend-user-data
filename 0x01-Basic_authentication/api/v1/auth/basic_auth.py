#!/usr/bin/env python3
'''create basic auth class'''

from api.v1.auth.auth import Auth
import re

class BasicAuth(Auth):
    '''basic auth'''
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        '''returns the base64 part of the auth header'''
        if authorization_header is None or (not isinstance(authorization_header, str)):
            return None
        pat = re.compile('Basic(.*) $')
        if not pat.match(authorization_header):
            return None
        tokens = authorization_header.split('Basic')
        return tokens[1]