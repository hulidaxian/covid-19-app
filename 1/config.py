import os

#配置相关
WTF_CSRF_ENABLED = True # CSRF prevention should be enabledSECRET_KEY = 'IefanWey' # key used to create cryptographically secure tokens


basedir = os.path.abspath(os.path.dirname(__file__))

#sqlite数据库配置相关
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'a secret string'

# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = os.environ.get("EMAIL_TODO")
# app.config['MAIL_PASSWORD'] = os.environ.get("PASSWORD_TODO")
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# app.config['SECRET_KEY'] = 'jfale!@#gys^&*(@jafd00193n'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False