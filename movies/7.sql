list all movies released in 2010 and their ratings, in descending order by rating.
with the same rating, order them alphabetically by title.
SELECT title, rating FROM 

 WHERE year = 2010 SORT BY rating
INNER JOIN ratings ON movies.id = ratings.movie_id
