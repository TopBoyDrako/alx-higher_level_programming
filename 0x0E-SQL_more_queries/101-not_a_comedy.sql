-- This script  lists all shows without the genre Comedy in the database

SELECT DISTINCT `title`
FROM `tv_shows` AS tv
  LEFT JOIN `tv_show_genres` AS tvshow
  ON tvshow.`show_id` = tv.`id`

  LEFT JOIN `tv_genres` AS genre
  ON genre.`id` = tvshow.`genre_id`
  WHERE tv.`title` NOT IN
    (SELECT `title`
    FROM `tv_shows` AS tv
      INNER JOIN `tv_show_genres` AS tvshow
      ON tvshow.`show_id` = tv.`id`

      INNER JOIN `tv_genres` AS genre
      ON genre.`id` = tvshow.`genre_id`
      WHERE genre.`name` = "Comedy"
    )
ORDER BY `title`;
