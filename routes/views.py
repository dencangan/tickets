from . import routes
from forms import CreateEvent
from flask import render_template
import models
from mainApp import db
import sqlite3

c = 'database/database.sqlite'


@routes.route('/')
@routes.route('/home')
def index():
    with sqlite3.connect(c) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM events")
        test = cur.fetchall()
    return render_template('index.html', test=test)


@routes.route('/events', methods=['GET', 'POST'])
def create_event():
    form = CreateEvent()
    db.create_all()
    try:
        if form.validate_on_submit():
            new_event = models.Events(
                event_name=form.event_name.data,
                event_date=form.event_date.data,
                event_tickets=form.event_tickets.data,
                redeemed_tickets=0
            )
            db.session.add(new_event)
            db.session.commit()
            print(f"New event created: \n{new_event}\n Saved in database.")

        else:
            print("something wrong happened")
    except Exception as e:
        print(e)

    return render_template('createEvents.html', title='Sign In', form=form)

