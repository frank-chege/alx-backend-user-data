#!/usr/bin/env python3
'''implement basic authentication'''
from flask import request
from typing import List, TypeVar

class Auth:
    '''manages api authentication'''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''require auth'''
        if path is None or excluded_paths is None or (len(excluded_paths) == 0):
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
    
    def authorization_header(self, request=None) -> str:
        '''auth header'''
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        '''current user'''
        return None