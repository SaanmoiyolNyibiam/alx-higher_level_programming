-- This is an SQL script that lists all shows contained in h
-- btn_0d_tvshows database that have at least one genre linked

SELECT title, tv_show_genres.genre_id
FROM tv_shows 
JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id 
ORDER BY title, tv_show_genres.genre_id;

