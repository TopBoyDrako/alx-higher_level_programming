-- This script lists all shows by their rating

SELECT title, SUM(`rate`) AS rates
FROM tv_shows AS tv
  INNER JOIN tv_show_ratings AS tvrating
  ON tv.id = tvrating.show_id
GROUP BY title
ORDER BY rates DESC;
