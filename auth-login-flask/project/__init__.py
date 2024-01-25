import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# init db to use it later in thr models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'thisasecretkey'
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # turn off autimatic changes "it used in Debuging"

    db.init_app(app)

    #login manager 
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' # the user will return to auth.login if he/she did not login if user trying to acess a protected route
    login_manager.init_app(app) # making the login_manager to work with the app concurnt with flask

    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

     # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    from .models import User



    #blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app 
