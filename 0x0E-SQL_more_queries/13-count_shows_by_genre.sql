-- count shows by genre
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS show_count 
FROM tv_genres, tv_show_genres, tv_shows 
WHERE tv_genres.id=tv_show_genres.genre_id and tv_shows.id = tv_show_genres.show_id 
GROUP BY tv_genres.name 
ORDER BY show_count DESC;
