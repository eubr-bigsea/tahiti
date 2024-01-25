"""" Module used in order to extract Marshmallow validation errors to pyBabel """
from gettext import gettext

def get_translations():
    return [
            gettext('Missing data for required field.'),
            gettext('Not a valid integer.'),
            gettext('Not a valid datetime.'),
            gettext("Not a valid boolean."),
            gettext('Must be one of:'),

    ]
