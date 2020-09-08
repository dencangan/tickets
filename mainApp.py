from flask import Flask
from routes import *
import json
import flask_sqlalchemy
import flask_migrate
import os


app = Flask(__name__)
app.register_blueprint(routes)

# Load json config
app_cfg = json.load(open("config.json"))

# Initialise flask config
for k, v in app_cfg.items():
    app.config[k] = v

db = flask_sqlalchemy.SQLAlchemy(app)

# Ensure database schema is up to date.
if os.path.exists('migrations'):
    print('Uprading DB to latest version.')
    with app.app_context():
        flask_migrate.upgrade()

if __name__ == '__main__':
    app.run(debug=False, port=5000, passthrough_errors=True)