import os
import redis
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand


app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_STRING')
db = SQLAlchemy(app)


# Setup migrate command for flask migrations through alembic
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


from mediastore.api import *
from mediastore.models import *