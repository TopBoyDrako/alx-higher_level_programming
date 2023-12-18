-- This script imports a database

SELECT tvshow.title, genre.genre_id
  FROM tv_shows AS tvshow
    INNER JOIN tv_show_genres AS genre
    ON tvshow.id = genre.show_id
  ORDER BY tvshow.title, genre.genre_id;
