from sys import argv, exit
from pymongo import Connection
from add_movie import add_movie

def init_movies(list): 
    # Initialize MongoDB connection and collection
    connection = Connection()
    db = connection.movies
    which_collection = db.owned_movies if (list == "owned") else db.towatch_movies

    movie_file = open(list + '.list', 'r')
    movies = [m.strip() for m in movie_file]
    for movie in movies:
        add_movie(movie, which_collection)

    # Clean up
    movie_file.close()
    
if __name__ == '__main__':
    if len(argv) != 2:
        print "Usage: init_movies.py owned/watch"
        exit(0)
    else:
        which_list = argv[1]
        init_movies(which_list)
