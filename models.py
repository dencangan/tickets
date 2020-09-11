from mainApp import db


class Events(db.Model):
    __tablename__ = "events"
    event_name = db.Column(db.String())
    event_date = db.Column(db.Integer())
    event_tickets = db.Column(db.Integer)
    ticket_id = db.Column(db.Integer, primary_key=True)
    ticket_code = db.Column(db.String())
    redeemed = db.Column(db.Boolean())

    def __repr__(self):
        return f"\n" \
               f"Event name: {self.event_name}\n" \
               f"Event Date: {self.event_date}\n" \
               f"Event tickets: {self.event_tickets}\n" \
               f"Ticket ID: {self.ticket_id}\n" \
               f"Ticket Code: {self.ticket_code}\n" \
               f"Redeemed tickets: {self.redeemed}" \
