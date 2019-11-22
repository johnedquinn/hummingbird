#####
# @file : reset.py
# @desc : Tests the ChartsController
# @author : TBD
#####

# IMPORTS
import cherrypy
import json
from database import database

# @class : ResetController
# @desc  : Resets the database
class ResetController(object):
    def __init__(self, db=None):
        if db is None:
            self.db = database()
        else:
            self.db = db

    def RESET_ALL(self):
        output = {'result' : 'success'}
        try:
            self.db.load_users('data/users.dat')
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)
