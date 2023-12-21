-- This script lists all shows and displays the number of shows
-- linked to each

SELECT g.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres AS g
  INNER JOIN tv_show_genres AS tvshow
  ON g.id = tvshow.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC
