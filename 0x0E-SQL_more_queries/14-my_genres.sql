-- This script lists all genres of the show Dexter

SELECT genre.name
FROM tv_genres AS genre
  INNER JOIN tv_show_genre AS tvshow
  ON genre.id = tvshow.genre.id
  INNER JOIN tv_shows AS tv
  ON tv.id = tvshow.show_id
  WHERE t.title = "Dexter"
ORDER BY genre.name
