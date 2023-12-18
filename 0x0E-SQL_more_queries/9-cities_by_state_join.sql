-- This script lists all cities in the database

SELECT cities.id, cities.name, states.name
  FROM cities AS city
    INNER JOIN states AS state
    ON cities.state_id = states.id
  ORDER BY cities.id ASC;
