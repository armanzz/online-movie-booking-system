# Online Movie Booking System

Type of input for the API

Parameter	Type	Description

Processes the movie title and returns result with all the necessary fields in a json format.

Output fields for the API for each Movie ID


## Steps to run
python:
- 3.7

git clone https://github.com/armanzz/online-movie-booking-system.git


install:
- pip install -r requirements.txt
- flask db init
- flask db migrate -m "Initial Migration"
- flask db upgrade
script:
- python -m flask test

