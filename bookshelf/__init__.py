from flask import Flask
from utils import get_instance_folder_path
from bookshelf.main.controllers import main
from bookshelf.admin.controllers import admin
from bookshelf.config import configure_app

app = Flask(__name__,
            instance_path=get_instance_folder_path(),
            instance_relative_config=True,
            template_folder='templates')

configure_app(app)

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')
