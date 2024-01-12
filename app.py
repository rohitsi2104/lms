"""
REF: https://github.com/hamzaavvan/library-management-system
"""
from flask import Flask
from Misc.functions import *
from core.config import config_instance


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = config_instance.secret_key
    app.config['MIN_EMAIL_LENGTH'] = config_instance.min_email_length
    app.config['MIN_PASSWORD_LENGTH'] = config_instance.min_password_length
    app.config['MIN_NAME_LENGTH'] = config_instance.min_name_length

    # app.config['SECRET_KEY'] = 'hardcoded_secret_key'
    # app.config['MIN_EMAIL_LENGTH'] = '20'
    # app.config['MIN_PASSWORD_LENGTH'] = '8'
    # app.config['MIN_NAME_LENGTH'] = '2'


    print("Secret Key:", app.config['SECRET_KEY'])
    print("Minimum Email Length:", app.config['MIN_EMAIL_LENGTH'])
    print("Minimum Password Length:", app.config['MIN_PASSWORD_LENGTH'])
    print("Minimum Name Length:", app.config['MIN_NAME_LENGTH'])

    app.app_context().push()
    # app.secret_key = '#$ab9&^BB00_.'
    # Registering blueprints
    from routes.user import user_view
    from routes.book import book_view
    from routes.admin import admin_view

    # Registering custom functions to be used within templates
    app.jinja_env.globals.update(
        ago=ago,
        str=str,
    )

    app.register_blueprint(user_view)
    app.register_blueprint(book_view)
    app.register_blueprint(admin_view)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)


