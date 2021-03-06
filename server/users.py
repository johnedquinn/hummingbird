#####
# @file : users.py
# @desc : API route for users
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
        self.db.load_users('data/users.dat')
        
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
        uid = int(uid)
        output = {'result': 'success'}
        try:
            user = self.db.get_user(uid)
            output['id'] = uid
            output['name'] = user['name']
            output['email'] = user['email']
            output['stocks'] = user['stocks']
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)         		
        return json.dumps(output)
    
    # @name : POST_USER
    # @desc : Add user
    # @body : user passes in { name, email, password, stocks }
    def POST_USER(self):
        output = {'result': 'success'}
        data = cherrypy.request.body.read()
        data = json.loads(data)
        totalUsers = len(self.db.users)
        print(data)
        try:
            output['id'] = totalUsers + 1
            output['name'] = data['name']
            output['email'] = data['email']
            output['stocks'] = data['stocks']
            set_user(totalUsers+1, data['name'], data['email'], data['password'], data['stocks'])
        except Exception as ex:
            output['result'] = 'error'
        return json.dumps(output)

    # @name : PUT_USER
    # @desc : Update  a user 
    # @body : {name, email, password, stocks} 
    def PUT_USER(self, uid):
        output = {'result': 'success'}
        data = cherrypy.request.body.read()
        data = json.loads(data)
        uid = int(uid)
        try: 
            self.db.set_user(uid, data['name'], data['email'], 'PASSWORD', data['stocks'])
        except Exception as ex: 
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)
         
    
    # @name : DELETE_USER
    # @desc : Delete a single user 
    def DELETE_USER(self,uid):
        output = {'result': 'success'}
        try: 
            self.db.delete_user(uid)
        except Exception as ex:
            output['result'] = 'error'
        return json.dumps(output)

    # @name : POST_STOCK 
    # @desc : update a stock 
    # @body : {uid, stock, amt}
    def POST_STOCK(self):
        output = {'result': 'success'}
        data = cherrypy.request.body.read()
        data = json.loads(data)
        try: 
            uid = data['uid']
            output['stock'] = data['stock']
            output['amt'] = data['amt']
            set_stock(uid,stock,amt)
        except Exception as ex: 
            output['result'] = 'error'
        return json.dumps(output)
