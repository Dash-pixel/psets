list the titles of all movies in which both Bradley Cooper and Jennifer Lawrence starred

SELECT title
FROM movies JOIN stars ON movies.id = stars.movie_id
WHERE stars.person_id IN (SELECT id FROM people WHERE name = 'Bradley Cooper');
//
SELECT title
FROM movies
WHERE id IN
(SELECT movie_id FROM stars JOIN people ON

WHERE name = 'Bradley Cooper');
(SELECT id FROM people WHERE name = 'Bradley Cooper');
