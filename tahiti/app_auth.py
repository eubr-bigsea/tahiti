# -*- coding: utf-8 -*-}
import json
import logging
import re
from collections import namedtuple
from functools import wraps
from keycloak import KeycloakOpenID

import requests
from flask import request, Response, current_app, g as flask_g

User = namedtuple("User",
                  "id, login, email, name, first_name, last_name, locale")

MSG1 = 'Could not verify your access level for that URL. ' \
       'You have to login with proper credentials provided by Lemonade Thorn'

MSG2 = 'Could not verify your access level for that URL. ' \
       'Invalid authentication token'

CONFIG_KEY = 'TAHITI_CONFIG'

log = logging.getLogger(__name__)

keycloak_openid = KeycloakOpenID(
    server_url="http://localhost:9080/auth/",
    client_id="tahiti-client",
    realm_name="thorn",
    client_secret_key="secret"
)


def authenticate(msg, params):
    """Sends a 403 response that enables basic auth"""
    return Response(json.dumps({'status': 'ERROR', 'message': msg}), 401,
                    mimetype="application/json")


def requires_auth(f):
    @wraps(f)
    def decorated(*_args, **kwargs):
        config = current_app.config[CONFIG_KEY]
        internal_token = request.args.get(
            'token', request.headers.get('x-auth-token'))
        token = request.headers.get('authorization').replace('Bearer ', '')
        user_id = request.headers.get('x-user-id')

        if token and user_id:
            try:
                userinfo = keycloak_openid.userinfo(token)

                setattr(flask_g, 'user', User(
                    id=userinfo['sub'],
                    name=userinfo['name'],
                    login=userinfo['email'],
                    email=userinfo['email'],
                    first_name=userinfo['given_name'],
                    last_name=userinfo['family_name'],
                    locale=''))

                return f(*_args, **kwargs)
            except:
                return authenticate(MSG2, {})

        # if token and user_id:
        #     expr = re.compile(r'Token token="?(.+?)"?, email="?(.+?)(?:"|$)')
        #     found = expr.findall(authorization)
        #     if not found:
        #         return authenticate(MSG2, {})
        #     token, email = found[0]
        #     # It is using Thorn
        #     url = '{}/api/tokens'.format(config['services']['thorn']['url'])
        #     payload = json.dumps({
        #         'data': {
        #             'attributes': {
        #                 'authenticity-token': token,
        #                 'email': email,
        #             },
        #             'type': 'tokens',
        #             'id': user_id
        #         }
        #     })
        #     headers = {
        #         'content-type': "application/json",
        #         'authorization': authorization,
        #         'cache-control': "no-cache",
        #     }
        #     r = requests.request("POST", url, data=payload,
        #                          headers=headers)
        #     if r.status_code != 200:
        #         if internal_token and internal_token == str(config['secret']):
        #             setattr(flask_g, 'user', User(2, '', '', '', '', ''))
        #             log.warn('Using Authorization and token is incorrect!')
        #             return f(*_args, **kwargs)
        #         else:
        #             print('Error in authentication ({}, {}, {}): {}'.format(
        #                 authorization, user_id, url, r.text))
        #             log.error('Error in authentication ({}, {}, {}): {}'.format(
        #                 authorization, user_id, url, r.text))
        #             return authenticate(MSG2, {})
        #     else:
        #         user_data = json.loads(r.text)
        #         setattr(flask_g, 'user', User(
        #             id=int(user_id),
        #             name='{} {}'.format(
        #                 user_data['data']['attributes']['first-name'].encode(
        #                     'utf8'),
        #                 user_data['data']['attributes']['last-name'].encode(
        #                     'utf8')),
        #             login=user_data['data']['attributes']['email'],
        #             email=user_data['data']['attributes']['email'],
        #             first_name=user_data['data']['attributes']['first-name'],
        #             last_name=user_data['data']['attributes']['last-name'],
        #             locale=''))
        #         return f(*_args, **kwargs)
        # elif internal_token:
        #     if internal_token == str(config['secret']):
        #         # System user being used
        #         setattr(flask_g, 'user', User(1, '', '', '', '', '', ''))
        #         return f(*_args, **kwargs)
        #     else:
        #         return authenticate(MSG2, {"message": "Invalid X-Auth-Token"})
        # else:
        #     return authenticate(MSG1, {'message': 'Invalid authentication'})

    return decorated
