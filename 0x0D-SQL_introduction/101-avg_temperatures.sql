-- This script displays the avg temp by a specific order

USE hbtn_0c_0;
SELECT city, AVG(temperatures) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
