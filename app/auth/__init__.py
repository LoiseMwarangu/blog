from flask import Blueprint

auth = Blueprint('auth',__name__)

from . import views,forms
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_simplemde import 
from . import views,forms


bootstrap = Bootstrap()

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

simple = SimpleMDE()


def create_app(config_name):

    app = Flask(__name__)

    # creating configurations
    app.config.from_object(config_options[config_name])


    # initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    simple.init_app(app)

    # registering main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # registering auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')

    # registering admin blueprint
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix = '/admin')


    return app


Add CommentCollapse 