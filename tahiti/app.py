#!/usr/bin/env python
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
        return request.args.get(
            'lang', 
                request.accept_languages.best_match(['en', 'pt', 'es']))


@app.route('/static/<path:path>')
def static_file(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    if app.debug:
        app.run(debug=True, host='0.0.0.0')
