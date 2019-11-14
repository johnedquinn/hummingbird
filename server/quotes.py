#####
# @file : quotes.py
# @desc : API route for quotes
# @author : TBD
#####

# IMPORTS
import cherrypy
import json
from database import database

# @class : QuotesController
# @desc  : route for quotes
class QuotesController(object):

    # @name : __init__
    # @desc : Constructor
    def __init__(self, db=None):
        if db is None:
            self.db = database()
        else:
            self.db = db
        
    # @name : GET_QUOTE
    # @desc : Gets a quote from the database
    def GET_QUOTE(self, symbol):
        output = { 'result': 'success' }
        try:
            quote = self.db.get_quote(symbol)
            print(quote)
            if quote is not None:
                output[symbol] = quote
            else:
                output['result'] = 'error'
                output['message'] = 'Quote not found'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)

    # @name : GET_QUOTES
    # @desc : Gets all quotes from the database
    def GET_QUOTES(self):
        output = { 'result': 'success' }
        try:
            quotes = self.db.get_quotes()
            output['quotes'] = quotes
        except Exception as ex:
            output['result'] = 'success'
            output['message'] = str(ex)
        return json.dumps(output)
