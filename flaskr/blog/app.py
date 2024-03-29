from flask  import Flask, render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app_vira=Flask(__name__)
app_vira.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///viradb.db"
db = SQLAlchemy(app_vira)
# create the app

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    
    def __repr__(self):
        return f'<user>  {self.username}  <email >  {self.email} ' 



@app_vira.route('/users')
def show_user():
    
    users_data=User.query.all()
    return render_template('about.html',user_data=users_data)

@app_vira.route('/')
def main_page():
    return render_template('home.html')

@app_vira.route('/about')
def about():
    return render_template('about.html')

@app_vira.route('/login/')
#@app_vira.route('/login/<int:id>')
@app_vira.route('/login/<id>')
def login_page(id=None):
    if id is None:return render_template('login.html',name='zeinab',family='fooladi',listcity=['a','b','c','d'])
    return f'this is login page {id}'




@app_vira.route('/all_user/<username>')
def say_hello(username):
    if username=='admin':
        return redirect(url_for('page_admin'))
    else:
        return redirect(url_for('page_users',username=username))


@app_vira.route('/admin/')
def page_admin():
    return f'hellooo admin'

@app_vira.route('/users/<username>')
def page_users(username):
    return f'hellooo user {username}'

