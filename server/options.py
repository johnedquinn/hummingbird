#####
# @file : options.py
# @desc : allows outside connections
# @author : TBD
#####

# IMPORTS
import cherrypy
import json
from database import database

# @class : OptionsController
# @desc  : allows outside connections
class OptionsController():
    def OPTIONS(self, *args, **kwargs):
        return ""