# My Sqreen
This project is a Flask app that listens for webhook notifications from a security application.

# Getting Started
To activate the virtual environment

`source venv/bin/activate`

To set up the Flask_APP environment variable

`export FLASK_APP=run.py`

To run the app

`flask run`


# Prerequisites
As the program is only a web server running locally in order to expose it to internet you have to install ngrok

`brew cask install ngrok`

It is running on http://localhost:5000/ so run

`./ngrok http 5000`

# Running the tests
The tests are built with the package unittest, to run them

`python -m unittest discover -s ./app -v`


# Built With
Flask

# Versioning
Git

# Author
Aude Rouaux

# License
This project is licensed under the MIT License - see the LICENSE.md file for details
