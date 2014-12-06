#!/usr/bin/python

"""
App builder. Can be imported and used to start the site
"""

from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from config import config


bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	
	db.init_app(app)
	
	from admin import admin
	admin.init_app(app)
	
	return app