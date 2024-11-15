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
        if path in excluded_paths:
            return False
        for excluded_path in excluded_paths:
            if exculded_path == path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization_header
            Return:
                None
        """
        if request is None:
            return None
        header = request.headers.get('Authorization')
        if header is None:
            return None
        return header

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user
            Return:
                None
        """
        return None
