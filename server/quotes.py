#####
# @file : quotes.py
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
        self.db.load_charts()
        
    # @name : GET_QUOTE
    # @desc : Gets a quote from the database
    def GET_QUOTE(self, symbol):
        output = { 'result': 'success' }
        try:
            quote = self.db.get_quote(symbol)
            if quote is not None:
                output[symbol] = quote
            else:
                output['result'] = 'error'
                output['message'] = 'Quote not found'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = 'GET_QUOTE: Exception thrown.'
        return output

    # @name : GET_QUOTES
    # @desc : Gets all quotes from the database
    def GET_QUOTES(self):
        output = { 'result': 'success' }
        try:
            quotes = self.db.get_quotes()
            output['quotes'] = quotes
        except Exception as ex:
            output['result'] = 'success'
        return output