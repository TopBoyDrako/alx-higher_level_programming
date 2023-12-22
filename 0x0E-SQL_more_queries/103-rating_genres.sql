-- This script lists all genres by their rating

SELECT `name`, SUM(`rate`) AS `rating`
  FROM `tv_genres` AS genre
       INNER JOIN `tv_show_genres` AS tvshow
       ON tvshow.`genre_id` = genre.`id`

       INNER JOIN `tv_show_ratings` AS rates
       ON rates.`show_id` = tvshow.`show_id`
 GROUP BY `name`
 ORDER BY `rating` DESC;
