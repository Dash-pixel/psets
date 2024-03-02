list the names of all people who starred in a movie in which Kevin Bacon also starred.
Be sure to only select the Kevin Bacon born in 1958.
Kevin Bacon himself should not be included in the resulting list.
SELECT name
FROM people JOIN stars ON people.id = stars.person_id
WHERE


birth = 1958
