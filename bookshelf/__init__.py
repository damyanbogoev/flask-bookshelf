from flask import Flask, render_template, request
from flask_security import current_user
from bookshelf.utils import get_instance_folder_path
from bookshelf.main.controllers import main
from bookshelf.admin.controllers import admin
from bookshelf.cache import cache
from bookshelf.config import configure_app
from bookshelf.data.models import db

app = Flask(__name__,
            instance_path=get_instance_folder_path(),
            instance_relative_config=True,
            template_folder='templates')

configure_app(app)
cache.init_app(app)
db.init_app(app)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error('Page not found: %s', (request.path, error))
    return render_template('404.htm'), 404

@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Server Error: %s', (error))
    return render_template('500.htm'), 500

@app.errorhandler(Exception)
def unhandled_exception(error):
    app.logger.error('Unhandled Exception: %s', (error))
    return render_template('500.htm'), 500

@app.context_processor
def inject_user():
    return dict(user=current_user)
