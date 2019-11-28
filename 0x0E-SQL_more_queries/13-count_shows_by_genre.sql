-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT  name as 'genre',
        count(*) as 'number_of_shows'
FROM    tv_genres, tv_show_genres
WHERE   tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.name
ORDER BY  number_of_shows DESC;
