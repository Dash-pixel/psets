list the names of all people who starred in a movie released in 2004, ordered by birth year.
No need to worry about people who have no birth year listed, so long as those who do have a birth year are listed in order.
If a person appeared in more than one movie in 2004, they should only appear in your results once.
SELECT UNIQUE name FROM people WHERE id = (SELECT person_id)
