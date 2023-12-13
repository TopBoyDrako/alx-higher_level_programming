-- This script displays the avg temp by a specific order

SELECT city AVG(temperature) AS average
FROM temperatures
GROUP BY city
ORDER BY average DESC;
