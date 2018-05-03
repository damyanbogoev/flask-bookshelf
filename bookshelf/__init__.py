from flask import abort, Flask, g, render_template, request, current_app
from flask_babel import Babel
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

babel = Babel(app)
configure_app(app)
cache.init_app(app)
db.init_app(app)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')


@app.url_defaults
def set_language_code(endpoint, values):
    if 'lang_code' in values or not g.get('lang_code', None):
        return
    if app.url_map.is_endpoint_expecting(endpoint, 'lang_code'):
        values['lang_code'] = g.lang_code


@app.url_value_preprocessor
def get_lang_code(endpoint, values):
    if values is not None:
        g.lang_code = values.pop('lang_code', None)


@app.before_request
def ensure_lang_support():
    lang_code = g.get('lang_code', None)
    if lang_code and lang_code not in app.config['SUPPORTED_LANGUAGES'].keys():
        abort(404)


@babel.localeselector
def get_locale():
    return g.get('lang_code', app.config['BABEL_DEFAULT_LOCALE'])


@babel.timezoneselector
def get_timezone():
    user = g.get('user', None)
    if user is not None:
        return user.timezone
    return "UTC"


@app.errorhandler(404)
def page_not_found(error):
    current_app.logger.error('Page not found: %s', (request.path, error))
    return render_template('404.htm'), 404


@app.errorhandler(500)
def internal_server_error(error):
    current_app.logger.error('Server Error: %s', (error))
    return render_template('500.htm'), 500


@app.errorhandler(Exception)
def unhandled_exception(error):
    current_app.logger.error('Unhandled Exception: %s', (error))
    return render_template('500.htm'), 500


@app.context_processor
def inject_data():
    return dict(user=current_user,
                lang_code=g.get('lang_code', None))


@app.route('/')
@app.route('/<lang_code>/')
@cache.cached(300)
def home(lang_code=None):
    return render_template('index.htm')


app.register_blueprint(main, url_prefix='/main')
app.register_blueprint(main, url_prefix='/<lang_code>/main')
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(admin, url_prefix='/<lang_code>/admin')
