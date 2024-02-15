-- a script that lists all genres in the
-- database hbtn_0d_tvshows_rate by their rating.
iSELECT tv_shows.title,
       SUM(tv_show_ratings.rate) AS rating
       FROM tv_shows
       INNER JOIN tv_show_ratings
       ON tv_show_ratings.show_id = tv_shows.id
       GROUP BY tv_shows.title
       ORDER BY rating DESC;
