-- This script lists all shows without a genre linked

SELECT tv_sho.title, genre.genre_id
FROM tv_shows AS tv_sho
  LEFT JOIN tv_show_genres AS genre
  ON tv_sho.id = genre.show_id
  WHERE genre.genre_id IS NULL
ORDER BY tv_show.title, genre.genre_id
