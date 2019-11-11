#####
# @file : movers.py
# @desc : API route for charts
# @author : TBD
#####

# IMPORTS
import cherrypy
import json
from database import database

# @class : ChartsController
# @desc  : route for charts
class MoversController(object):

    # @name : __init__
    # @desc : Constructor
    def __init__(self, db=None):
        if db is None:
            self.db = database()
        else:
            self.db = db
        self.db.load_movers()
        
    # @name : GET_MOVERS
    # @desc : Gets all charts from the database
    def GET_MOVERS(self):
        output = { 'result': 'success' }
        return json.dumps(output)