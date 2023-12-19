from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


SQLALCHEMY_DATABASE_URI = 'sqlite:///items_database.db'
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = "login_bp.login"
