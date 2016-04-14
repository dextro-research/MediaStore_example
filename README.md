# MediaStore_example
Media Storage Service

## Installation

To install dependencies create a virtual environment with virtualenv and install using ```python setup.py install```

Requires a postgres database with appropriate permissions.  Before the app can be tested, the database must be bootstrapped.  In order to do this:
```
1.  Install the dependencies as stated above
2.  Open a python terminal 
3.  Execute the following code

> from mediastore import db
> db.create_all()

4.  This should return without error.  If you log in to the database via psql or another tool, you should see the 3 tables specified in the models.py file, Media, Entity, and Entities
```

## Required ENV variables
DATABASE_STRING -> postgres connection string
ENVIRONMENT -> either Development or Production depending on deployment


## Running a Development Server
To start a development server run ```python run_webserver.py```


## Production Server
A production server requires some python compatible server to handle requests - this can be something like Gunicorn or uWSGI - which is often, but not required to be proxied through something like Nginx or Apache


## Routes
There are 2 main routes.
GET requests to /media - which should return the list of currently annotated media
POST requests to /media - which will store annotations for a selected media - raw json parameters are expected i.e.
```{ "media_url": "my_media_url1.com", "entities": ["car", "boat", "plane"]```


