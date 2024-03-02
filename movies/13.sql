list the names of all people who starred in a movie in which Kevin Bacon also starred.
Be sure to only select the Kevin Bacon born in 1958.
Kevin Bacon himself should not be included in the resulting list.

SELECT name
FROM stars JOIN people ON stars.person_id = people.id
WHERE stars.movie_id IN
(SELECT stars.movie_id FROM stars JOIN people ON stars.person_id = people.id WHERE name = 'Kevin Bacon' AND birth = 1958)
AND name != 'Kevin Bacon';;









SELECT name
FROM stars JOIN people ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
WHERE


(SELECT id WHERE name = 'Kevin Bacon' AND birth = 1958)
