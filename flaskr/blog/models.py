from blog import db,login_manager
import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    

class User (db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password=db.Column(db.String(60), nullable=False)
    posts=db.relationship('Post',backref='auther',lazy=True)
    def __repr__(self):
        return f' {self.__class__.__name__} {self.username}  <email >  {self.email} ' 


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(120), nullable=False)
    date=db.Column(db.DateTime, nullable=False,default=datetime.datetime.now)
    content=db.Column(db.Text, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    
    def __repr__(self):
        return f'< {self.__class__.__name__} <id==>> {self.id}  <title >  {self.title} ' 
