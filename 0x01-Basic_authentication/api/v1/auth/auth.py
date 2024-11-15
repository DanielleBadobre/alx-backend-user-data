#!/usr/bin/env python3
""" a class to manage the API authentication.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    class for authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth
            Return:
                False
        """
        if path is None:
            return True
        if not excluded_paths:
            return True
        if path[-1] != '/':
            path += '/'
        for excluded_path in excluded_paths:
            if exculded_path == path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization_header
            Return:
                None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user
            Return:
                None
        """
        return None
