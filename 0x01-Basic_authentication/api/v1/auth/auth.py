#!/usr/bin/env python3
""" a class to manage the API authentication.
"""
from flask import request
from flask import List, TypeVar


class Auth:
    """class for authentication
        Return:
            a
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth
            Return:
                False
        """
        return False

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
