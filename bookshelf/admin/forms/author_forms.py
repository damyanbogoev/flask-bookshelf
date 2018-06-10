from wtforms import Form, TextField, validators
from flask_babel import lazy_gettext as _


class CreateAuthorForm(Form):
    names = TextField(_('Names'), [validators.Length(min=5, max=70)])
