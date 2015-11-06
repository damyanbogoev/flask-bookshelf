from wtforms import Form, TextField, validators

class CreateAuthorForm(Form):
    names = TextField('Names', [validators.Length(min=5, max=70)])
