
from mainApp import db


class Events(db.Model):
    __tablename__ = "events"
    event_name = db.Column(db.String())
    event_date = db.Column(db.String())
    event_tickets = db.Column(db.Integer, primary_key=True)
    redeemed_tickets = db.Column(db.Integer)

    def __repr__(self):
        return f"\n" \
               f"Event name: {self.event_name}\n" \
               f"Event Date: {self.event_date}\n" \
               f"Event tickets: {self.event_tickets}" \
               f"Redeemed tickets: {self.redeemed_tickets}" \


# class Tickets(db.Model):
#     __tablename__ = "tickets"
#     ticket_code = db.Column(db.String())
#     event_tickets = db.Column(db.Integer, primary_key=True)
#     redeemed = db.Column(db.Boolean())
#
#     def __repr__(self):
#         return f"\n" \
#                f"Event name: {self.event_name}\n" \
#                f"Event Date: {self.event_date}\n" \
#                f"Event tickets: {self.event_tickets}" \
#                f"Tickets redeemed: {self.redeemed_tickets}"
