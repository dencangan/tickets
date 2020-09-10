import os
from routes import *
from flask import Flask
import flask_sqlalchemy
import flask_migrate
from hashids import Hashids

app = Flask(__name__)
app.register_blueprint(routes)

_ROOT = os.path.abspath(os.path.dirname(__name__))
_ROOT = _ROOT.replace("\\", "\\\\")

app_cfg = {"SECRET_KEY": "something_else",
           "HASHIDS_SALT": "zk4UcRMgy3jJBx0dVMn2dIy0",
           "HASHIDS_LENGTH": 8,
           "HASHIDS_ALPHABETS": "abcdefghijklmnopqrstuvwxyz0123456789",
           "SQLALCHEMY_DATABASE_URI": 'sqlite:///' + _ROOT + '\\\\database.sqlite',
           "SQLALCHEMY_TRACK_MODIFICATIONS": False}

# Initialise flask config
for k, v in app_cfg.items():
    app.config[k] = v

db = flask_sqlalchemy.SQLAlchemy(app)
hashids = Hashids(salt=app.config['HASHIDS_SALT'],
                  min_length=app.config['HASHIDS_LENGTH'],
                  alphabet=app.config['HASHIDS_ALPHABETS'])

# Ensure database schema is up to date.
if os.path.exists('migrations'):
    print('Uprading DB to latest version.')
    with app.app_context():
        flask_migrate.upgrade()

if __name__ == '__main__':
    app.run(debug=False, port=5000, passthrough_errors=True)