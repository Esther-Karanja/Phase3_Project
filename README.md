# Phase3_project
This project uses Python Fire which is a Python library to turn a Python component into a command line interface with just a single call to Fire. It uses SQLAlchemy ORM external library to create database tables and uses Alembic to manage database tables and schemas.Alembic is a library for handling schema changes that uses SQLAlchemy to perform the migrations in a standardized way.

The project has 3 tables

## Instructions
To get started, run `pipenv install` then `pipenv shell` to create a virtual environment from which the app
is built using

Then run `pipenv alembic sqlalchemy` to install dependancies needed for the project

Then run `alembic init migrations` to create a migration environment in the migrations/directory. This process creates our migration environment as well as an `alembic ini` with configuration options from the environment.

Then configure a migration environment by changing important settings in the `alembic.ini` and `env.py` files to work with our database. in `alembic.ini` change the url to `sqlalchemy.url = sqlite:///models.db` and then configure the `env.py` file to point to the metadata attribute of our new declarative_base object using 
`from models import Base`
`target_metadata = Base.metadata`

### Migrations
After adding our data model to `models.py` , we run the commands `alembic revision --autogenerate -m "commit message"` for the migration. During autogeneration, Alembic inspects the metadata of Base in `models.py`, comparing it to the current state of the database

Then run the autogenerated migration to create the table from the previous step ie`alembic upgrade head`

### Object Relationships

This project contains 3 classes `Lablel`, `Artist` and `Song`. 
`Label` and `Song` have a one-to-many relationship with the `label` having mant `artists`
`Artist` and `Song` have a many-to-many relationship with an `artist` having many `songs` and a `song` can have many `artists`

The `artist.py` file contains python classes, `models.py` contains SQLAlchemy tables and `cli-script.py` contains the CLI scripts

## License
    Copyright (C) 2023  Esther Karanja

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

## Author
Esther Karanja , an upcoming full-stack software engineer

