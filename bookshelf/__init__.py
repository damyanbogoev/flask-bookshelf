from flask import Flask
from utils import get_instance_folder_path
from bookshelf.main.controllers import main
from bookshelf.admin.controllers import admin

app = Flask(__name__,
            instance_path=get_instance_folder_path(),
            instance_relative_config=True,
            template_folder='templates')

app.config.from_object('bookshelf.config.DevelopmentConfig')
app.config.from_pyfile('config.cfg', silent=True)

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')
