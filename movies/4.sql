SELECT COUNT(*) FROM movies WHERE id = (SELECT movie_id FROM ratings WHERE rating = 10);
SELECT title FROM movies WHERE id = (SELECT movie_id FROM ratings WHERE rating = 10);
SELECT title FROM movies WHERE id = (SELECT movie_id FROM ratings WHERE rating = 10);
SELECT title UNION
FROM movies WHERE id = (SELECT movie_id FROM ratings WHERE rating = 10);
