from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object('config')
Bootstrap(app)

# Create database connection object
db = SQLAlchemy(app)

from .home.views import home
from .static import global_static
from .auth import auth
app.register_blueprint(home)
app.register_blueprint(global_static,static_folder='static')
app.register_blueprint(auth)