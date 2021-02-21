import logging
from flask import Flask, request, json
from digiez_api.views import *
from digiez_api.oop_views import *
from digiez_api.extensions import db


def create_app(config_module):
    # Create app and set config
    app_ = Flask(__name__)
    app_.config.from_object(config_module)
    app_.secret_key = '3?\xbf\xc2\x8b\xa9k\xe5\xef\xc5(\x9b_\xf6\xd1\tp {*\x0cV\x91\x81'
    # Init DB
    db.init_app(app_)
    # Blueprints
    app_.register_blueprint(web.web)
    # Account is done with another approach:
    # Http's methods are defined in a class thank to flask-restful package
    # app_.register_blueprint(api_accounts.api_accounts)
    app_.register_blueprint(api_malls.api_malls)
    app_.register_blueprint(api_units.api_units)
    app_.register_blueprint(docs.docs)
    #OOP VIEWS
    app_.register_blueprint(oop_api_accounts.api_accounts)
    return app_


# Create Flask app
app = create_app('digiez_api.config.ConfigEnv')


@app.before_first_request
def setup_tables_db():
    db.create_all()
    db.session.commit()
