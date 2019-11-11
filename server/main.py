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
from database import database

# @name : start_service
# @desc : starts the server
def start_service():
    
    # Setup dispatcher and database
	dispatcher = cherrypy.dispatch.RoutesDispatcher()
	db = database()
 
	# Initialize Controllers
	chartsController = ChartsController(db=db)
	moversController = MoversController(db=db)

	# Connect the routes
	dispatcher.connect('c_get_charts', '/charts/', controller=chartsController, action='GET_CHARTS', conditions=dict(method=['GET']))
	dispatcher.connect('c_get_chart', '/charts/:symbol', controller=chartsController, action='GET_CHART', conditions=dict(method=['GET']))
	dispatcher.connect('m_get_movers', '/movers/', controller=moversController, action='GET_MOVERS', conditions=dict(method=['GET']))
 
	# Server configuration
	conf = {
			'global' : {
				'server.socket_host' : 'student04.cse.nd.edu',
				'server.socket_port' : 51075,
				},
			'/' : {'request.dispatch' : dispatcher}
			}
	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config=conf)
	cherrypy.quickstart(app)

# @name : main
# @desc : main driver for file
if __name__ == '__main__':
	start_service()
