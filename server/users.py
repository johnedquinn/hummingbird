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
class UsersController(object):

    # @name : __init__
    # @desc : Constructor
    def __init__(self, db=None):
        if db is None:
            self.db = database()
        else:
            self.db = db
        self.db.load_users()
        
    # @name : GET_USERS
    # @desc : Gets all users
    def GET_USERS(self):
        output = { 'result': 'success' }
        try:
            users = self.db.get_users()
            output['users'] = users
        except Exception as ex:
            output['result'] = 'error'
        return json.dumps(output)

    # @name : GET_USER
    # @desc : Get a single user
    def GET_USER(self , uid):
        output = {'result': 'success'}
        try:
            user = self.db.get_user(uid)
            output['id'] = uid
            output['name'] = user['name']
            output['email'] = user['email']
            output['stocks'] = user['stocks']
        except Exception as ex:
            output['result'] = 'error'
        return json.dumps(output)
    
    # @name : POST_USER
    # @desc : Add user
    # @body : user passes in { name, email, password, stocks }
    def POST_USER(self):
        data = cherrypy.request.body.read()
        data = json.loads(data)
        try:
            # @TODO
        except Exception as ex:
            # @TODO
        return json.dumps(output)

    # @name : PUT_USER
    # @desc : Update  a user 
    # @body : {uid, name, email, password, stocks} 
    def PUT_USER(self):
	data = cherrypy.request.body.read()
	data = json.loads(data)
	try: 	
    
        
    # @name : DELETE_USER
    # @desc : Delete a single user 
    def DELETE_USER(self,uid):
        output = {'result': 'success'}
        try: 
            self.db.delete_user(uid)
        except Exception as ex:
            output['result'] = 'error'
        return json.dumps(output)

    # @name : DELETE_STOCK
    # @desc : Delete a single stock
    # @body : user passes in body {stock}
    '''def DELETE_STOCK(self, uid):
	data = cherrypy.request.body.read()
	data = json.loads(data)
	stock = data['stock']
        output = {'result': 'success'}
        try: 
            self.db.delete_stock(uid, stock)
        except Exception as ex:
            output['result'] = 'error'
        return json.dumps(output)'''
