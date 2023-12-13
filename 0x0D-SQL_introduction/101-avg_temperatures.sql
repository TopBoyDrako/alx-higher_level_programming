-- This script displays the avg temp by a specific order

SELECT city, AVG(temperatures) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
