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

Reference:
https://docs.djangoproject.com/en/3.0/ref/models/fields/
https://docs.google.com/document/d/1dTbL_GFY4UTfZzhZOvZFihed1t2qu0SUb0qIo6HvE_0/edit


Might design using tailwing(https://tailwindcss.com/) or bootstrap

### Architecture

#### Models:

- User
    - name - this is intended to be for the parent or whoever is in charge of taking care and setting rules
    - will need to be able to fill out data-base/API from UI, and have it be unique for each user. Admin site should be for me only, but user will need to be able to update their own set of rules and kids

    - can maybe use the built in user model from permissions?

    - foreign keys pointing to kid and rules

- Kid
    - name
        - string
    - points counter - influenced by rules
        - int

- Rule
    - will need a "weight" value/points value
        - int
    - name
        - string
    - description
        - string
    - will need to be assigned to kids somehow

I'll need a model relationship diagram here

## User stories

[-] as a user, I want a personalized account so that I can keep track of my set of kids and rules
[-] as a user, I want to be able to assign points to kids based on rules/chores, so I can check how they're keeping up with stuff at a glance
