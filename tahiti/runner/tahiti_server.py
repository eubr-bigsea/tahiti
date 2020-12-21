#!/usr/bin/env python
# -*- coding: utf-8 -*-
# noinspection PyBroadException
try:
    import eventlet

    eventlet.monkey_patch(all=True, thread=True)
except:
    print('Error in monkey patch')
import argparse

import eventlet.wsgi
from flask import request, g
from flask_babel import get_locale

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", type=str,
                        help="Config file", required=True)
    args = parser.parse_args()

    from tahiti.factory import create_app, create_babel_i18n

    app = create_app(config_file=args.config)
    babel = create_babel_i18n(app)
    config = app.config['TAHITI_CONFIG']
    port = int(config.get('port', 5000))


    @babel.localeselector
    def get_locale_from_query():
        return request.args.get('lang', 'en')


    @app.before_request
    def func():
        g.locale = get_locale()


    @app.route('/static/<path:path>')
    def static_file(path):
        return app.send_static_file(path)


    if app.debug:
        app.run(debug=True)
    else:
        eventlet.wsgi.server(eventlet.listen(('', port)), app)
