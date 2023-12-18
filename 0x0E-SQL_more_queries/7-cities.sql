-- This script creates a database and table with specifications

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENTED PRIMARY KEY,
    state_id INT NOT NULL
    FOREIGN KEY (state_id) REFERENCES states(id)
    name VARCHAR(256) NOT NULL
);
