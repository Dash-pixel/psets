list the names of all people who starred in a movie in which Kevin Bacon also starred.
Be sure to only select the Kevin Bacon born in 1958.
Kevin Bacon himself should not be included in the resulting list.
SELECT name
FROM
FROM people JOIN stars ON people.id = stars.person_id
WHERE stars.movie_id IN


birth = 1958

SELECT id WHERE name = 'Kevin Bacon' AND birth = 1958
