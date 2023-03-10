#!/usr/bin/env python
# -*- coding: utf-8 -*-
# noinspection PyBroadException
try:
    #import eventlet

    #eventlet.monkey_patch(all=True, thread=False)
    pass
except:
    pass
from flask import request, g
from flask_babel import get_locale

from tahiti.factory import create_app, create_babel_i18n

app = create_app()

babel = create_babel_i18n(app)

@babel.localeselector
def get_locale_from_query():
    try:
        return g.user.locale
    except:
        try:
            return request.args.get('lang', 'en')[:2]
        except:
            return 'en'


@app.route('/static/<path:path>')
def static_file(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    if app.debug:
        app.run(debug=True, host='0.0.0.0')
