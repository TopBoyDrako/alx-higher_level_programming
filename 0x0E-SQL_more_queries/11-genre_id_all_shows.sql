-- This script lists all shows in the database

SELECT tv_sho.title, genre.genre_id
  FROM tv_shows AS tv_sho
  LEFT JOIN tv_show_genres AS genre
  ON tv_sho.id = genre.show_id
ORDER BY sho.title, genre.genre_id;
