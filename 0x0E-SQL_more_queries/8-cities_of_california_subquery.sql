-- This script lists all cities of a state in the database

SELECT cities
FROM states
WHERE name = California
ORDER BY cities.id ASC
