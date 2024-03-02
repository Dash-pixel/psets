list the titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated.
You may assume that there is only one person in the database with the name Chadwick Boseman.

SELECT title FROM movies
WHERE id IN (SELECT movie_id FROM stars WHERE person_id IN
(SELECT id FROM people WHERE name = 'Chadwick Boseman'));
