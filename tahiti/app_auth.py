# -*- coding: utf-8 -*-}
import json
import logging
import re
from collections import namedtuple
from functools import wraps

import requests
from flask import request, Response, current_app, g as flask_g

User = namedtuple(
    "User", "id, login, email, name, first_name, last_name, " + 
    "locale, permissions,roles")

MSG1 = 'Could not verify your access level for that URL. ' \
       'You have to login with proper credentials provided by Lemonade Thorn'

MSG2 = 'Could not verify your access level for that URL. ' \
       'Invalid authentication token'

CONFIG_KEY = 'TAHITI_CONFIG'

log = logging.getLogger(__name__)


def authenticate(msg, params):
    """Sends a 403 response that enables basic auth"""
    return Response(json.dumps({'status': 'ERROR', 'message': msg}), 401,
                    mimetype="application/json")

def requires_permission(*permissions):
    def real_requires_permission(f):
        @wraps(f)
        def decorated(*_args, **kwargs):
            fullfill = len(set(permissions).intersection(
                    set(flask_g.user.permissions))) > 0
            if fullfill:
                return f(*_args, **kwargs)
            else:
                return Response(
                    json.dumps({'status': 'ERROR', 'message': 'Permission'}),
                    401,
                    mimetype="application/json")

        return decorated

    return real_requires_permission


def requires_auth(f):
    @wraps(f)
    def decorated(*_args, **kwargs):
        config = current_app.config[CONFIG_KEY]
        if str(config.get('secret', '')) == request.headers.get(
                'X-Auth-Token'):
            # Inter services authentication
            setattr(flask_g, 'user', User(0, 'internal', 
                'lemonade@lemonade.org.br', 'internal', 'en', '', '', 
                permissions=[], roles=[]))
            return f(*_args, **kwargs)
        else:
            user_id = request.headers.get('x-user-id')
            permissions = request.headers.get('x-permissions')
            roles = request.headers.get('x-roles')
            user_data = request.headers.get('x-user-data')
    
            if all([user_data, user_id]):
                login, email, name, locale = user_data.split(';')
                parts = name.split(' ', 1)
                setattr(flask_g, 'user', 
                        User(int(user_id), login, email, name, parts[0], 
                            parts[1].strip() if len(parts)> 1 else '', 
                            locale, permissions=(permissions or '').split(','),
                            roles=(roles or '').split(',')))
                return f(*_args, **kwargs)
            else:
                return authenticate(MSG1, {'message': 'Invalid authentication'})

    return decorated



