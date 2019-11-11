#!/usr/bin/env python3

class server:

	def __init__(self):
		self.movies = {}

	def load_movies(self, movie_file):
		self.movies = {}
		f = open(movie_file)
		for line in f:
			line = line.rstrip()
			components = line.split("::")
			mid = int(components[0])
			mname = components[1]
			mgenres = components[2]

			self.movies[mid] = [mname, mgenres]
		f.close()

	def print_sorted_movies(self):
		for mid, movie in sorted(self.movies.items()):
			print(movie)

	def get_movie(self, mid):
		mid = int(mid)
		if mid in self.movies.keys():
			return self.movies[mid]
		return None

	def get_movies(self):
		mids = []
		for mid in sorted(self.movies.keys()):
			mids.append(mid)
		return mids

	def set_movie(self, mid, info):
		self.movies[mid] = info

	def delete_movie(self, mid):
		self.movies.pop(mid, None)

	def load_users(self, users_file):
		self.users = {}
		f = open(users_file)
		for line in f:
			line = line.rstrip()
			components = line.split("::")
			uid = int(components[0])
			ugender = components[1]
			uage = int(components[2])
			uocc = int(components[3])
			uzip = components[4]

			self.users[uid] = [ugender, uage, uocc, uzip]
		f.close()
	
	def get_user(self, uid):
		if uid in self.users.keys():
			return self.users[uid]
		return None

	def get_users(self):
		return(self.users.keys())

	def set_user(self, uid, info):
		self.users[uid] = info

	def delete_user(self, uid):
		if(uid in self.users.keys()):
			del self.users[uid]

	def load_ratings(self, ratings_file):
		f = open(ratings_file)
		ratings = {}
		for line in f:
			line = line.rstrip()
			components = line.split("::")
			uid = int(components[0])
			mid = int(components[1])
			urating = int(components[2])

			if mid in self.ratings:
				self.ratings[mid][uid] = urating
			else:
				self.ratings[mid] = {uid: urating}
		f.close()

	def get_rating(self, mid):
		cumulative = 0
		if mid in self.ratings.keys():
			for rating in self.ratings[mid].values():
				cumulative += rating
			return cumulative / len(self.ratings[mid])
		return None

	#TODO return None if no object data??????????
	def get_highest_rated_movie(self):
		topMovie = 0
		topRating = -1
		for movie in sorted(self.ratings):
			avgRating = self.get_rating(movie)
			if(avgRating > topRating):
				topMovie = movie
				topRating = avgRating
		return(topMovie)
	
	def get_highest_rated_unvoted_movie(self, uid):
		uid = int(uid)
		topMovie = 0
		topRating = -1
		for movie in sorted(self.ratings):
			avgRating = self.get_rating(movie)
			if(avgRating > topRating and uid not in self.ratings[movie]):
				#print("{}: {}".format(movie, avgRating))
				topMovie = movie
				topRating = avgRating
		return(topMovie)

	def set_user_movie_rating(self, uid, mid, rating):
		self.ratings[mid][uid] = rating
	
	def get_user_movie_rating(self, uid, mid):
		if mid not in self.ratings:
			return None
		if uid not in self.ratings[mid]:
			return None
		return self.ratings[mid][uid]

	def delete_all_ratings(self):
		self.ratings = {}
  
	def load_posters(self, file):
		self.posters = {}
		f = open(file)
		for line in f:
			line = line.rstrip()
			components = line.split("::")
			id = int(components[0])
			mid = int(components[1])
			path = components[2].rstrip()
			self.posters[id] = path
		f.close()
      
	def get_poster_by_mid(self, mid):
		mid = int(mid)
		if mid in self.posters.keys():
			return self.posters[mid]
		return '/default.jpg'

if __name__ == "__main__":
	mdb = _movie_database()

	#### MOVIES ########
	mdb.load_movies('ml-1m/movies.dat')
	mdb.load_users('ml-1m/users.dat')
	mdb.load_ratings('ml-1m/ratings.dat')
	rating = mdb.get_rating(787)
	print(rating)
	mdb.set_user_movie_rating(41, 787, 2)
	rating = mdb.get_rating(787)
	print(rating)

