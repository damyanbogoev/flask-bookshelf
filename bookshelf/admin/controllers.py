from flask import Blueprint, render_template, request, flash
from bookshelf.admin.forms.author_forms import CreateAuthorForm
from bookshelf.data.models import Author, db


admin = Blueprint('admin', __name__, template_folder='templates')


@admin.route('/')
def index():
    return render_template('admin_index.htm')


@admin.route('/author/create', methods = ['GET', 'POST'])
def create_author():
    form = CreateAuthorForm(request.form)
    if request.method == 'POST' and form.validate():
        author = Author(form.names.data)
        db.session.add(author)
        flash('Author successfully created.')
        return redirect(url_for('main.display_authors'))
    return render_template('create_author.htm', form=form)