from flask import render_template, flash, redirect, url_for, session
from flask_login import login_user, current_user, logout_user, login_manager,LoginManager
from flask_mail import Message
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from app import app,db
from flask_bootstrap import Bootstrap
from .database import User
from .form import RegisterForm, LoginForm, ForgotPasswordForm, ResetPasswordForm

bcrypt = Bcrypt(app)
mail = Mail(app)
bootstrap = Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
@app.route('/home')
@app.route('/')
def home():
    return render_template('index.html', title="Home")


# 注册
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(email=form.email.data, username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html', form=form, title='Sign Up')

# 登陆
@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for("home"))
        flash("User does not exist, or invalid username or password.", 'warning')
    return render_template("login.html", form=form, title="Login")

# 忘记密码
@app.route("/forgotpassword", methods=["GET", "POST"])
def forgot_password():
    form = ForgotPasswordForm()
    if current_user.is_authenticated:
        return redirect(url_for('userhome'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash("An email has been sent to reset your password.", 'success')


    return render_template("forgotpw.html", form=form, title="Forgot Password")

# 重置密码
@app.route("/resetpassword/<token>", methods=["GET", "POST"])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('userhome'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('forgot_password'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('resetpw.html', title='Reset Password', form=form)

#退出登陆
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


# 重置邮箱
def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Forgot your password?',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
    {url_for('reset_password', token=token, _external=True)}
If you did not make this request then simply ignore this email.
'''
    mail.send(msg)

#登陆用户
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#请求前置处理
@app.before_request
def make_session_permanent():
    session.permanent = True

# 错误处理404
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 Page Not Found</h1>", 404

# 错误处理403
@app.errorhandler(403)
def page_not_found(e):
    return "<h1>403 You do not have permission to do that.</h1>", 403

