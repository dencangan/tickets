# Tickets and Events Manager App
This is a rudimentary events and tickets manager designed using the Python flask framework with RESTful API implementation.

## How to Set Up and Run
Setting up a python virtual environment
1. Create the virtual environment: python -m venv <YOUR-ENV-NAME>
2. Activate the virtual environment: <YOUR-ENV-NAME>\Scripts\activate
3. Get list of dependencies from 'requirements.txt' and use pip to install them: pip install -r requirements.txt
4. Once the environment + packages are set up, enter 'git clone https://github.com/dencangan/tickets.git' in command prompt/powershell or git bash to clone remote repository to your local machine.
5. Run 'mainApp.py' to launch the app.
  
For windows, use command prompt and cd to repository directory. Then enter "python mainApp.py".
For mac, 


## Overview
### Flask forms and Database
The app is form based, and with each submission of a form, a database query is executed to ensure the database is updated to reflect the changes we see in the app.

The database used is SQLite3 for ease in portability and presenting concepts. There is only one table called "events" in the database which contains the event details as well as its ticket code. 

When a ticket is redeemed, the database will look for the specific code redeemed and update the row as 1 (redeemed) from the default of 0 (not redeemed) in the redeemed column.

The ticket table in the events page is the database table visualised in 2D form. Any query related actions on the app will reflect on this table. This serves as a tracker and tool to ensure the logic of the app is correct. It should be part of an admin page, hidden away from the public.

### Ticket Codes and Hash Identifiers
The ticket codes are generated using hash identifiers (hashids). A hashid is a unique string of characters, generated for each ticket when an event is created. This is to ensure no two events share the same ticket code. 

For example, the first event created will have 5 tickets, identified as ticket #0 to #4. when we create the next event of another 5 tickets, the identifiers will be ticket #5 to #9. This increasing order will always ensure that which each identifier, a unique hashid will be generated and assigned to the ticket.

### Home Page
This is where you can track the max amount of tickets set for an event and the amount of tickets redeemed.

### Tickets Page 
Here you can redeem a ticket, or check if the ticket is valid.
By entering a ticket code in addition to the existing link it will return the jsonified data of the ticket, ie, tickets/<ticket_code>.

### Events Page
In this page, you can:
- Create a new event.
- Delete an existing one.
- Add tickets to an existing event.
- View the ticket record table.

## Limitations
To maintain simplicity, both event data and ticket code data are put in the same database table. If handling hundreds of events and thousands of tickets, it is more practical to have multiple tables containing different kinds of data, and a layer of concatenation to piece them together.

If you have any issues, please contact me at dencan.gan@gmail.com
