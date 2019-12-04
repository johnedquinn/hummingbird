#####
# @file : main.py
# @desc : The main driver for our application. Creates the routes for ...
# ... all API calls
# @author : TBD
#####

# IMPORTS
import cherrypy
from charts import ChartsController
from movers import MoversController
from quotes import QuotesController
from users import UsersController
from reset import ResetController
from options import OptionsController
from database import database

# @name : CORS
# @desc : creates accessibility
def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"
    cherrypy.response.headers["Access-Control-Allow-Credentials"] = "true"

# @name : start_service
# @desc : starts the server
def start_service():

    # Setup dispatcher and database
    dispatcher = cherrypy.dispatch.RoutesDispatcher()
    db = database()
 
    # Initialize Controllers
    chartsController = ChartsController(db=db)
    moversController = MoversController(db=db)
    quotesController = QuotesController(db=db)
    usersController = UsersController(db=db)
    resetController = ResetController(db=db)
    optionsController = OptionsController()

    # Connect the routes
    dispatcher.connect('c_get_chart', '/charts/:symbol', controller=chartsController, action='GET_CHART', conditions=dict(method=['GET']))
    dispatcher.connect('m_get_movers', '/movers/', controller=moversController, action='GET_MOVERS', conditions=dict(method=['GET']))
    dispatcher.connect('q_get_quote', '/quotes/:symbol', controller=quotesController, action='GET_QUOTE', conditions=dict(method=['GET']))
    dispatcher.connect('q_get_quotes', '/quotes/', controller=quotesController, action='GET_QUOTES', conditions=dict(method=['GET']))
    dispatcher.connect('u_get_users', '/users/', controller=usersController, action='GET_USERS', conditions=dict(method=['GET']))
    dispatcher.connect('u_get_user', '/users/:uid', controller=usersController, action='GET_USER', conditions=dict(method=['GET']))
    dispatcher.connect('u_post_user', '/users/', controller=usersController, action='POST_USER', conditions=dict(method=['POST']))
    dispatcher.connect('u_put_user', '/users/:uid', controller=usersController, action='PUT_USER', conditions=dict(method=['PUT']))
    dispatcher.connect('u_delete_user', '/users/:uid', controller=usersController, action='DELETE_USER', conditions=dict(method=['DELETE']))
    dispatcher.connect('u_post_stock', '/users/stock/', controller=usersController, action='POST_STOCK', conditions=dict(method=['POST']))
    dispatcher.connect('u_reset_all', '/reset/', controller=resetController, action='RESET_ALL', conditions=dict(method=['PUT']))

    dispatcher.connect('o_get_chart', '/charts/:symbol', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('o_get_movers', '/movers/', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('o_get_quote', '/quotes/:symbol', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('o_get_quotes', '/quotes/', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('o_get_users', '/users/', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('o_get_user', '/users/:uid', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('o_post_stock', '/users/stock/', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('o_reset_all', '/reset/', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    
    # Server configuration
    conf = {
            'global' : {
                'server.socket_host' : 'student04.cse.nd.edu',
                'server.socket_port' : 51075,
                },
            '/' : {
                'request.dispatch' : dispatcher,
                'tools.CORS.on' : True
                }
            }
    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)

# @name : main
# @desc : main driver for file
if __name__ == '__main__':
    cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
    start_service()
