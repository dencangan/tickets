# Tickets and Events Manager App
This is a rudimentary events and tickets manager designed using the Python flask framework with RESTful API implementation.

## Run - Docker
This app is dockerised. However, you can also set it up manually without docker following the instructions below in Windows or Mac (see wiki page). See end of README for additional docker notes.
https://hub.docker.com/repository/docker/dencangan/tickets


## Run - Without Docker 
### Windows
1. Once the environment + packages are set up, enter 'git clone https://github.com/dencangan/tickets.git' in command prompt/powershell or git bash to clone remote repository to your local machine.
2. Open command prompt and cd to repo directory. Enter "python mainApp.py". For Mac/Linux, "python ./mainApp.py".

## Overview
### Flask forms and Database
The app is form based, and with each submission of a form, a database query is executed to ensure the database is updated to reflect the changes we see in the app.

The database used is SQLite3. There is only one table called "events" in the database which contains event details and ticket codes. 

When a ticket is redeemed, the database will look for the specific code redeemed and update the row as 1 (redeemed) from the default of 0 (not redeemed) in the 'redeemed' column.

The ticket table in the 'events' page is the database table visualised in 2D form. Any query related actions on the app will reflect on this table. This serves as a tracker and tool to ensure the logic of the app is correct.

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
- To maintain simplicity, both event data and ticket code data are put in the same database table. If handling hundreds of events and thousands of tickets, it is more practical to have multiple tables containing different kinds of data, and a layer of concatenation to piece them together.
- To have a date picker instead of entering integers as dates.

## Additional Docker notes when dockerising the app
1. Clone the repository from Github.
2. Open powershell and cd to repository directory.
3. Create Dockerfile and open up with any editor and enter the following:

FROM python:3.7
WORKDIR /tickets
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "mainApp.py"]

### Build the image
docker build --tag {imagename:tag} .

### Run the app and test it
docker run -p 5000:5000 {imagename:tag}

### Pushing image to Docker Hub
docker tag bulletinboard:1.0 {Your Docker ID}/{imagename:tag}

docker push {Your Docker ID}/{imagename:tag}

### Deleting images
Ensure no containers are running.
docker images -a
docker rmi {imagename:tag}

### Delete all images
docker system prune -a

### Delete container
docker rm --force {imagename:tag}
