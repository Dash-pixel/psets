SELECT SUM(rating)/ COUNT(rating) FROM ratings WITH movie_id IN (SELECT id FROM movies WITH year = 2012);
In 6.sql, write a SQL query to determine the average rating of all movies released in 2012.
