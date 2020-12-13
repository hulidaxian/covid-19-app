from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, ValidationError, Email

from app.database import User

#注册
class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email(message="Invalid Email"), Length(max=50)],
                        render_kw={"placeholder": "example@gmail.com"})
    username = StringField("Username", validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=4, max=15)],
                             render_kw={"placeholder": "********"})
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(username=username.data).first()
        if existing_user_username:
            raise ValidationError("That username already exists. Please choose a different one.")

    def validate_email(self, email):
        existing_user_email = User.query.filter_by(email=email.data).first()
        if existing_user_email:
            raise ValidationError("That email address belongs to different user. Please choose a different one.")

#登陆
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=4, max=15)])
    submit = SubmitField('Login')

#新建待办
class NewTodoForm(FlaskForm):
    todo = TextAreaField("Enter Todo", validators=[InputRequired(), Length(min=4, max=130)])
    submit = SubmitField("Create Todo")

#编辑待办
class EditTodoForm(FlaskForm):
    todo = TextAreaField("Enter Todo", validators=[InputRequired(), Length(min=4, max=130)])
    submit = SubmitField("Edit Todo")

#忘记密码
class ForgotPasswordForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email(message="Invalid Email"), Length(max=50)])
    submit = SubmitField('Submit')

#重置密码
class ResetPasswordForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email(message="Invalid Email"), Length(max=50)])
    # username = StringField("Username", validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=4, max=15)])
    submit = SubmitField('Reset Password')