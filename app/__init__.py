"""Main init file to initialise all Flask related packages and create the app."""

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
import sqlite3

db = SQLAlchemy()


def create_app(config_class=Config):
    """
    Function that will be called on the main app module. This function initialises all flask related packages,
    load config, as well as the set blueprints in the app.
    """

    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # Create event table for the first time
    conn = sqlite3.connect("database.sqlite")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS events (event_name TEXT, event_date TEXT,
    event_tickets INTEGER, ticket_id INTEGER PRIMARY KEY, ticket_code TEXT, redeemed INTEGER);''')
    conn.commit()
    conn.close()

    return app


from app import forms