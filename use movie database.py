
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="MongoDB_2",
    database="movie"
)

mycursor = mydb.cursor()
query1="SELECT NAME,VOTES FROM MOVIE_ID ORDER BY VOTES DESC LIMIT 8"
mycursor.execute(query1)
result=mycursor.fetchall()


moviename=[]

for i in result:
    moviename.append(i)
print(moviename)
