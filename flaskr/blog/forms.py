from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from blog.models import User,Post
from flask_login import current_user


class RegistrationForm(FlaskForm):
    username=StringField('نام کاربری',validators=[DataRequired(),Length(min=4,max=25,message='نام کاربری باید بیش از 4 کارکتر و کمتر از 25 کارکتر باشد')])
    email = StringField('ایمیل', validators=[DataRequired(), Email(message='ایمیل خود را درست وارد کنید')])
    password=PasswordField('رمز عبور',validators=[DataRequired()])
    confirm_password=PasswordField('تکرار رمز عبور',validators=[DataRequired(),EqualTo('password',message='پسورد شما یکسان وارد نشده است')] )
    submit=SubmitField('ثبت')
    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('این نام کاربری قبلا ثبت شده است')
    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('این ایمیل قبلا ثبت شده است')
    
class LoginForm(FlaskForm):
    email = StringField('ایمیل', validators=[DataRequired(),  Email(message='ایمیل خود را درست وارد کنید')])
    password=PasswordField('رمز عبور',validators=[DataRequired()])
    remember=BooleanField(label='مرا به خاطر بسپار')
    submit=SubmitField('ورود')
    
class UpdateProfileForm(FlaskForm):
    username=StringField('نام کاربری',validators=[DataRequired(),Length(min=4,max=25,message='نام کاربری باید بیش از 4 کارکتر و کمتر از 25 کارکتر باشد')])
    email = StringField('ایمیل', validators=[DataRequired(), Email(message='ایمیل خود را درست وارد کنید')])
    
    submit=SubmitField('به روزرسانی')
    def validate_username(self,username):
        if username.data!= current_user.username:
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('این نام کاربری قبلا ثبت شده است')
    def validate_email(self,email):
        if email.data!= current_user.email:
            user=User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('این ایمیل قبلا ثبت شده است')
    
class PostForm(FlaskForm):
    title=StringField('Title',validators=[DataRequired()])
    content=TextAreaField('Content',validators=[DataRequired()])
    