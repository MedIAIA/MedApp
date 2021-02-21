MedAssessment
=====================

Running App using Docker:
> docker build -t mydigiez .
> docker run -d -p 5001:5001 mydigiez

Running App using virtual env:
> sudo apt-get install python3-pip
> sudo pip3 install virtualenv
> python -m venv env
> pip install -r requirements.txt
> sudo apt-get install sqlite3 
> sqlite3 app.db < data/dump.sql
> pytest
> python runserver.py


Migrations are like version control for your database, 
allowing your team to easily modify and share the application's database schema. .
Run migrations initialization, using the db init command as follows:
> python migrate.py db init

Migration script will generate the tables that will persist.
> Run the migration:
> python migrate.py db migrate

Launch automated test:
> pytest