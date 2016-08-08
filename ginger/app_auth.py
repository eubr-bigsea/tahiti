# -*- coding: utf-8 -*-}
from functools import wraps

from flask import request, Response


def check_auth(token):
    return token == '123456'


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*_args, **kwargs):
        # auth = request.authorization
        token = (request.json and request.json.get('token')) or \
                request.args.get('token') or \
                request.headers.get('X-Auth-Token')
        if not (token and check_auth(token)):
            return authenticate()
        return f(*_args, **kwargs)

    return decorated
