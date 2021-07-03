# Basic Django and Postgres Project

Learning some basic django and postgres. Based on https://www.enterprisedb.com/postgres-tutorials/how-use-postgresql-django 


## Requirements

- Python installed
- PostgresSQL installed
## Setup

### Set up python environment for django.

```bash

$ cd django-postgres

# create a virtual environment
$ python -m venv venv

# install requirements
$ pip -r requirements.txt

```

### Setup  postgres database

Assuming your database server is running:

```bash
$ createdb myfirstdb

# create a user for the database called django and set password 
$ createuser django -P

```

Next we use Django to activate the [car models](./backend/cars/models.py) and create the table in postgres.

```bash
$ python manage.py makemigrations cars

$ python manage.py migrate cars
```

Next we need to add some data to our database. I did this in two ways but others are available:

```psql
# first by just inserting rows into the cars_drivers table
myfirstdb=# INSERT INTO cars_driver(name, licence)
myfirstdb=# VALUES ('Bob blue','X321');
myfirstdb=# INSERT INTO cars_driver(name, licence)
myfirstdb=# VALUES ('Gary Grey','Y321')
```

Next we load the `cars_car` table from a csv file.

```psql
myfirstdb=# COPY cars_car FROM '/full/path/to/data/car-data.csv'
myfirstdb=# DELIMITER ','
myfirstdb=# CSV HEADER;

```
