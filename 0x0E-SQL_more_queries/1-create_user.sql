-- This script creates a new user and grants privileges

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'IDENTIFIED BY 'user_0d_1_pwq';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;	
FLUSH PRIVILEGES;
