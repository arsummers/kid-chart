# kid-chart
This is going to be the web-app version of kid chart.
Current goal is to make this into a usuable django site, then make a django rest framework version to feed into a mobile-app friendly front-end.

Don't forget about Docker

will need to use
`poetry export -f requirements.txt -o requirements.txt`
since I'm using poetry instead of pip
don't forget to test this too
remember httpie

docker-compose up --build
docker-compose down
docker-compose restart
docker-compose exec web ./manage.py migrate
docker-compose exec web ./manage.py collectstatic

Stretch goal:
Ability to log in as a kid vs carer

Absolutely going to need to be able to customize what user accounts can see and add to in the database.

Profiles for each kid - maybe like a summary page of each kid's points and actions?


### Architecture

#### Models:

- User
    - name - this is intended to be for the parent or whoever is in charge of taking care and setting rules
    - will need to be able to fill out data-base/API from UI, and have it be unique for each user. Admin site should be for me only, but user will need to be able to update their own set of rules and kids

    - can maybe use the built in user model from permissions?

    - foreign keys pointing to kid and rules

- Kid
    - name
    - points counter

- Rule
    - will need a "weight" value/points value
    - name
    - description