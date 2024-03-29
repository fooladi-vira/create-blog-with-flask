from flask  import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app=Flask(__name__)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message='ابتدا وارد حساب خود شوید'
login_manager.login_message_category='info'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../viradb.db"
app.config['SECRET_KEY']='a26e0c6fca70230695b5d9d3e2246947'
db=SQLAlchemy(app)
from blog import routes
