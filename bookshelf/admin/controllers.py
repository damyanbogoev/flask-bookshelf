from flask import Blueprint, render_template, flash, current_app
from flask import Blueprint, redirect, request, url_for, flash
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
    	names = form.names.data
    	current_app.logger.info('Adding a new author %s.', (names))
        author = Author(names)
        db.session.add(author)
        db.session.commit()
        flash('Author successfully created.')

        return redirect(url_for('main.display_authors'))

    return render_template('create_author.htm', form=form)