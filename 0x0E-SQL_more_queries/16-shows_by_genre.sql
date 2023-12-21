-- This script lists all shows, and genres linked to that show, from the database

SELECT tv.title, genre.name
FROM tv_shows AS tv
  LEFT JOIN tv_show_genres AS show
  ON tv.id = show.show_id

  LEFT JOIN tv_genres AS genre
  ON show.genre_id = genre.id
ORDER BY tv.title, genre.name;
