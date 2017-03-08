#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
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
