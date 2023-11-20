from flask_babel import gettext
def translate_validation(validation_errors):
    for field, errors in list(validation_errors.items()):
        validation_errors[field] = [gettext(error) for error in errors]
    return validation_errors

class DataConsistencyError(Exception):
    """ Exception for lack of consistency on data sent by user that it is not captured by ValidationError (editing step id that is not associated with certain pipeline)"""
    def __init__(self, message) -> 'DataConsistencyError':
        self.message = message