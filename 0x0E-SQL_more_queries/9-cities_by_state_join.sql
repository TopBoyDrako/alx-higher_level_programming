-- This script lists all cities in the database

SELECT city.id, city.name, state.name
  FROM cities AS city
    INNER JOIN states AS state
    ON city.state_id = state.id
  ORDER BY city.id ASC;
