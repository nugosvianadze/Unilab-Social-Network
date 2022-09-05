
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
login_manager = LoginManager()

csrf = CSRFProtect()

db = SQLAlchemy()
migrate = Migrate()