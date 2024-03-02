list the titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated.
Your query should output a table with a single column for the title of each movie.
You may assume that there is only one person in the database with the name Chadwick Boseman.

SELECT title FROM movie
WHERE id IN (SELECT person_id FROM directors
WHERE movie_id IN (SELECT movie_id FROM ratings WHERE rating >= 9.0));
