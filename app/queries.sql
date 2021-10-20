-- name: get_movie_with_id^
-- Get a movie with the given title_id
SELECT * FROM titles WHERE title_id = :title_id;