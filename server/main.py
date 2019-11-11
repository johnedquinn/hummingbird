import cherrypy

# create movies.py, users.py, etc. in the curr dir
from ./routes/api/charts import ChartsController

# copy your fully working python primer
from server import server

def start_service():
	dispatcher = cherrypy.dispatch.RoutesDispatcher()

	# instantiate mdb so that it is shared with all controllers

	mdb_o = _movie_database()

	# instantiate controllers
	movieController = MovieController(mdb=mdb_o)
	userController  = UserController(mdb=mdb_o)
	voteController  = VoteController(mdb=mdb_o)
	ratingController = RatingController(mdb=mdb_o)
	resetController = ResetController(mdb=mdb_o)

	#connecting endpoints

	#connect /movies/:movie_id resource
	dispatcher.connect('m_get_movie', '/movies/:mid', controller=movieController, action='GET_MOVIE', conditions=dict(method=['GET']))
	dispatcher.connect('m_get_movies', '/movies/', controller=movieController, action='GET_MOVIES', conditions=dict(method=['GET']))
	dispatcher.connect('m_put_movie', '/movies/:mid', controller=movieController, action='PUT_MOVIE', conditions=dict(method=['PUT']))
	dispatcher.connect('m_post_movie', '/movies/', controller=movieController, action='POST_MOVIE', conditions=dict(method=['POST']))
	dispatcher.connect('m_delete_movie', '/movies/:mid', controller=movieController, action='DELETE_MOVIE', conditions=dict(method=['DELETE']))
	dispatcher.connect('m_delete_movies', '/movies/', controller=movieController, action='DELETE_MOVIES', conditions=dict(method=['DELETE']))
	
	dispatcher.connect('user_get_uid', '/users/:user_id', controller=userController, action='GET_UID', conditions=dict(method=['GET']))
	dispatcher.connect('user_put_uid', '/users/:user_id', controller=userController, action='PUT_UID', conditions=dict(method=['PUT']))
	dispatcher.connect('user_delete_uid', '/users/:user_id', controller=userController, action='DELETE_UID', conditions=dict(method=['DELETE']))
	
	dispatcher.connect('user_get_all', '/users/', controller=userController, action='GET_ALL', conditions=dict(method=['GET']))
	dispatcher.connect('user_post_all', '/users/', controller=userController, action='POST_ALL', conditions=dict(method=['POST']))
	dispatcher.connect('user_delete_all', '/users/', controller=userController, action='DELETE_ALL', conditions=dict(method=['DELETE']))
	
	dispatcher.connect('rec_get_uid', '/recommendations/:user_id', controller=voteController, action='GET_UID', conditions=dict(method=['GET']))
	dispatcher.connect('rec_put_uid', '/recommendations/:user_id', controller=voteController, action='PUT_UID', conditions=dict(method=['PUT']))
	dispatcher.connect('rec_delete_all', '/recommendations/', controller=voteController, action='DELETE_ALL', conditions=dict(method=['DELETE']))
	
	dispatcher.connect('ratings_get', '/ratings/:mid', controller=ratingController, action='GET_RATING', conditions=dict(method=['GET']))
	
	dispatcher.connect('user_reset_all', '/reset/', controller=resetController, action='PUT_INDEX', conditions=dict(method=['PUT']))
	dispatcher.connect('user_reset_mid', '/reset/:movie_id', controller=resetController, action='PUT_MID', conditions=dict(method=['PUT']))

	conf = {
			'global' : {
				'server.socket_host' : 'student04.cse.nd.edu',
				'server.socket_port' : 51033,
				},
			'/' : {'request.dispatch' : dispatcher}
			}

	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config=conf)
	cherrypy.quickstart(app)


if __name__ == '__main__':
	start_service()
