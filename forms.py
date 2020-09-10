from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, Length, NumberRange


class CreateEvent(FlaskForm):
    event_name = StringField('Name of Event', validators=[
        DataRequired(message='Please enter a valid event name.'),
        Length(max=320, message='Your event name must be less than ' + str(320) + ' characters.')
    ])
    event_date = StringField('Date of Event', validators=[
        DataRequired(message='Please enter date of event.'),
        Length(max=200, message="Your date must be less than " + str(200) + " characters.")
    ])
    event_tickets = IntegerField('Set number of tickets', validators=[
        DataRequired(message='Please number of tickets.'),
        NumberRange(min=1,  max=500, message="Invalid number.")
    ])
    submit = SubmitField('Create Event')


class RedeemTickets(FlaskForm):
    ticket_code = StringField('Enter ticket code', validators=[
        DataRequired(message='Please enter a valid ticket_code.'),
        Length(max=9, message='Your ticket must be less than 9 characters.')
    ])
    submit = SubmitField('Redeem Ticket')


class CheckTickets(FlaskForm):
    ticket_check = StringField('Check ticket code', validators=[
        DataRequired(message='Please enter a valid ticket_code.'),
        Length(max=9, message='Your ticket must be less than 9 characters.')
    ])
    submit = SubmitField('Check Ticket')


class AddTickets(FlaskForm):
    add_tickets_event = StringField('Enter event name to add tickets', validators=[
        DataRequired(message='Please enter valid event.'),
        Length(max=320, message='Your ticket must be less than 9 characters.')
    ])

    new_tickets = IntegerField('Number of tickets to add', validators=[
        DataRequired(message='Please number of tickets.'),
        NumberRange(min=1,  max=500, message="Invalid number.")
    ])

    submit = SubmitField('Add Tickets')


class DeleteEvents(FlaskForm):
    delete_event = StringField('Enter event name', validators=[
        DataRequired(message='Please enter valid event.'),
        Length(max=320, message='Your ticket must be less than 9 characters.')
    ])
    submit = SubmitField('Delete Event')