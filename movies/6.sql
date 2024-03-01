SELECT SUM(rating)/ COUNT(rating) FROM ratings WHERE movie_id IN (SELECT id FROM movies WHERE year = 2012);
In 6.sql, write a SQL query to determine the average rating of all movies released in 2012.
