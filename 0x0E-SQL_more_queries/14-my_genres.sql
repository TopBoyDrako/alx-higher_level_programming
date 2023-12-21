-- This script lists all genres of the show Dexter

SELECT genre.name
FROM tv_genres AS genre
  INNER JOIN tv_show_genres AS tvshow
  ON genre.id = tvshow.genre_id
  INNER JOIN tv_shows AS tv
  ON tv.id = tvshow.show_id
  WHERE tv.title = "Dexter"
ORDER BY genre.name;
