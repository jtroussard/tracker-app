# Fitness Tracker

Welcome to the super simple fitness tracker! This is intended more to be a simple journaling tool for weight loss or other fitness/physical goals. It is still currently in development so there might still be some small bugs. Another motivation for creating this app is as an exercise in full stack web development, however! contributions, and feedback greatly appreciated.

## Installation

1. Clone this repository:  
`git clone https://github.com/jtroussard/tracker-app.git`

2. Navigate into the project directory:  
`cd tracker-app`

3. It is recommended to build inside a vitrual environment, this step is optional:  
`python3 -m venv venv && source venv/bin/activate`

4. Install the required packages:  
`pip install -r requirements.txt`

## Usage

To run the application, execute the following command from the root directory of the project:  
`python run.py` or `python3 run.py` depeneding on your aliases (requires Python 3.X)

The application will now be running at `http://localhost:8888/`.

## Testing

To run unit tests, execute the following command from the root directory of the project:
`make test`

## Linting

To run linting using pylint, execute the following command from the root directory of the project:
`pylint app/`

## Screen Shots

![Home page screen shot](https://user-images.githubusercontent.com/17488893/236649128-bf59156f-55e3-4cc0-bf8d-b11ed2aba2dc.png)
![Account page screen shot](https://user-images.githubusercontent.com/17488893/236649161-be239b64-56c7-4720-94ca-2a997bc9c162.png)
![Entries page screen shot](https://user-images.githubusercontent.com/17488893/236649173-d1129a48-59be-405c-b175-1aa14233b559.png)
![Registration page screen shot](https://user-images.githubusercontent.com/17488893/236649178-34096d12-e427-4b0d-8647-d5aa93206ab6.png)

## Attributions

### Photos
https://www.publicdomainpictures.net/en/browse-author.php?a=87

## Where I left off/Things I need to attend to
* LEFT OFF: got the migration from flask container to db container working, migrate said out of date so i just ran upgrade, checked the db container looks ok went to app added user logged in added entry. looks good. need to finish crud tests then review the dev env configs and figure out the volume stuff.

* figure out volumes
* crud tests in dev
* cron in db container for back ups

* another bug - saving entry shows success and warn at the same time

* confirm authentication method for postgresql (need version number, then check pg_hba.conf)
* I think the db user set in the compose file is the power user, so make sure that the db init scripts create the limited user for the app and that matches what is in the app configuration, DONT accidentally set it to the power user.

## Headaches for me (Delete when pipeline and base features are done)
### When I run the docker container of this application alone I can't connect via the browser
* check logs to make sure the app started without errors: `docker logs "container name"
* if there are no errors make sure the docker run command adds the port mapping to the exposed port then try again

## Useful commands to remember
*docker-compose -f ./Docker/docker-compose.dev.yml up -d