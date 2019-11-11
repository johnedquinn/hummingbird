#incomplete code
#movies.py

import cherrypy
import json
from _movie_database import _movie_database

class MovieController(object):

    # @name : INIT
    # @desc : Constructor
    def __init__(self, mdb=None):
        if mdb is None:
            self.mdb = _movie_database()
        else:
            self.mdb = mdb

        self.mdb.load_movies('ml-1m/movies.dat')
        self.mdb.load_posters('ml-1m/images.dat') 

    # @name : GET_MOVIE
    # @desc : Gets movie using MID
    def GET_MOVIE(self, mid):
        # Create output and take in MID
        output = {'result' : 'success'}
        mid = int(mid)
        # Try to get data
        try:
            movie = self.mdb.get_movie(mid)
            img = self.mdb.get_poster_by_mid(mid)
            if movie is not None:
                output['id']        = mid
                output['title']     = movie[0]
                output['genres']    = movie[1]
                output['img']       = img
            else:
                output['result'] = 'error'
                output['message'] = 'movie not found'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)
    
    # @name : GET_MOVIES
    # @desc : Gets all movies
    def GET_MOVIES(self):
        output = {}
        try:
            output["movies"] = []
            mids = self.mdb.get_movies()
            for id in mids:
                #if id is not None:
                insert = {}
                movie = self.mdb.get_movie(id)
                img = self.mdb.get_poster_by_mid(id)
                title = movie[0]
                genres = movie[1]
                insert["title"] = title
                insert["genres"] = genres
                insert["result"] = "success"
                insert["id"] = int(id)
                insert["img"] = img
                output["movies"].append(insert)
            output['result'] = 'success'
        except Exception as ex:
            output['result'] = 'error'
        return json.dumps(output)

    # @name : PUT_MOVIE
    # @desc : Edit movie in database
    def PUT_MOVIE(self, mid):
        # Precursors
        output = {'result': 'success'}
        mid = int(mid)
        # Get request body
        data = cherrypy.request.body.read()
        print(data)
        data = json.loads(data)
        try:
            self.mdb.set_movie(mid,[data['title'], data['genres']])
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)
    
    # @name : POST_MOVIE
    # @desc : Adds a new movie to the movies dictionary
    def POST_MOVIE(self):
        # Create output message and grab request body
        output = {'result' : 'success'}
        data = cherrypy.request.body.read()
        data = json.loads(data)
		# Try to update movie
        try:
            movies = list(self.mdb.get_movies())
            mid = int(movies[-1]) + 1
            output["id"] = mid
            refinedData = [data["title"], data["genres"]]
            self.mdb.set_movie(mid, refinedData)
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)
		
    # @name : POST_MOVIE
    # @desc : Adds a new movie to the movies dictionary
    def DELETE_MOVIE(self, mid):
        output = {'result': 'success'}
        mid = int(mid)
        try:
            self.mdb.delete_movie(mid)
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
            
        return json.dumps(output)
    
    # @name : POST_MOVIE
    # @desc : Adds a new movie to the movies dictionary
    def DELETE_MOVIES(self):
        output = {'result': 'success'}
        try:
            self.mdb.movies = {}
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)


if __name__ == '__main__':
    mc = MovieController()
    mc.GET_MOVIES()