from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, Length, NumberRange


class CreateEvent(FlaskForm):
    event_name = StringField('Event Name', validators=[
        DataRequired(message='Please enter a valid event name.'),
        Length(max=320, message='Your event name must be less than ' + str(320) + ' characters.')
    ])

    event_date = StringField('Event Date', validators=[
        DataRequired(message='Please enter date of event.'),
        Length(max=200, message="Your date must be less than " + str(200) + " characters.")
    ])

    event_tickets = IntegerField('Number of tickets', validators=[
        DataRequired(message='Please number of tickets.'),
        NumberRange(min=1,  max=500, message="Invalid number.")
    ])

    submit = SubmitField('Create Event')
