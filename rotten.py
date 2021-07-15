import imdb

hr=imdb.IMDb()
mname = input("enter a movie: ")
movies=hr.search_movie(mname)
index=movies[0].getID()
movie=hr.get_movie(index)

print(movie['director'][0])

#for i in movie['director']:
 #   print(i['name'])


