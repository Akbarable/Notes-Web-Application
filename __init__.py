from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from os import path
from flask_login import LoginManager, login_manager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    #initializing flask application 
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'qwerty'

    # telling flask where the sqlalchemy database is stored
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

     #initializing database
    db.init_app(app)


    from .views import views
    from .auth import auth
   

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    from .models import User, Note

    create_database(app)

   

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    #telling flask how to load a user (by default will look for PK )
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app

#function to create a db, if one does not exist
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Database Created!')

