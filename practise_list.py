# -*- coding: utf-8 -*-
movies = ["Coco", "Harry Potter", "英雄", "Speeding"]
print (len(movies))
print ('\n')

movies.insert(1, "Mexico")
for each_movie in movies:
    print (each_movie)
print ('\n')

movies.extend(["Me Before You", "捉妖记2"])
count = 0
while count < len(movies):
    print (movies[count])
    count += 1
print ('\n')

print (movies.pop(3))
print (movies)
print ('\n')

movies.remove("捉妖记2")
print (movies)
