#####
# @file : users.py
# @desc : API route for quotes
# @author : TBD
#####

# IMPORTS
import cherrypy
import json
from database import database

# @class : ChartsController
# @desc  : route for charts
class ChartsController(object):

    # @name : __init__
    # @desc : Constructor
    def __init__(self, db=None):
        if db is None:
            self.db = database()
        else:
            self.db = db
        self.db.load_users()