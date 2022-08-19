from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = 'c09ede5df1bd3b1c377d385c6b2bd937'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nfynwnadwnmlzq:83e03f98e8195b551cbaa967b31cb67cf64c682467720b592495cac2b07e9a17@ec2-3-208-79-113.compute-1.amazonaws.com:5432/d4jmpblpe3k253'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

from comunidadeflask import routes

