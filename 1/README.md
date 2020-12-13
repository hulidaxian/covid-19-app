This is a Todo list app where you can create todo's.
You can sign up and then make todo's. You have the option
to delete them and to complete them once they have been completed.


Made in:
Python 3.7.9


Libraries:
1. Flask
2. flask_sqlalchemy
3. flask_wtf
4. flask_bootstrap
5. wtforms
6. wtforms.validators
7. flask_login
8. flask_bcrypt



Database:
sqlite3


ORM:
SQLAlchemy


File Structure:
1. main.py - Main app file (Everything is in here)
2. templates/base.html - Template that all other templates inherit from.
3. templates/index.html - Home/Landing page of the app.
4. templates/mytodos.html - Page that shows all of your todo's. This also shows the options to mark as complete and delete.
5. templates/newtodos.html - Page where you can create a new todo.
6. static/style.css - CSS file
7. database.db - Database
8. README.md - File that contains all of the information about the app (This file).


Mac Installations:
1. pip3 install Flask
2. pip3 install flask_sqlalchemy
3. pip3 install flask_bootstrap
4. pip3 install flask_wtf
5. pip3 install wtforms
6. pip3 install flask_login
7. pip3 install flask_bcrypt

Windows Installations:
1. pip install Flask
2. pip install flask_sqlalchemy
3. pip install flask_bootstrap
4. pip install flas_wtf
5. pip install wtforms
6. pip install flask_login
7. pip install flask_bcrypt