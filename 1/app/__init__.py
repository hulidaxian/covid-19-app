from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#初始化相关
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

migrate = Migrate(app, db)
from app import view,todolist