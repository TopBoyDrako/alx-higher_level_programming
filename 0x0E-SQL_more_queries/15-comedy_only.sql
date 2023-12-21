-- This script lists all Comedy shows in the database

SELECT tv.title
FROM tv_shows AS tv
  INNER JOIN tv_show_genres AS tvshow
  ON tv.id = tvshow.show_id
  INNER JOIN tv_genres AS genre
  ON genre.id = tvshow.genre_id
  WHERE genre.name = "Comedy"
ORDER BY tv.title;
