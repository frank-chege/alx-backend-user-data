#!/usr/bin/env python3
'''authenticates a user's session'''

from .auth import Auth
import uuid

class SessionAuth(Auth):
    '''authenticates a user's session'''
    user_id_by_session_id = {}
    def create_session(self, user_id: str = None) -> str:
        '''creates a user's session id'''
        if user_id is None or (not isinstance(user_id, str)):
            return None
        session_id = uuid.uuid4()
        self.user_id_by_session_id[session_id] = user_id
        return session_id