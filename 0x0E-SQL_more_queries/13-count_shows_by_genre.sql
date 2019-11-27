-- count shows by genre
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS count_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id=tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY count_shows DESC;
