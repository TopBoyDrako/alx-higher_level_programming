-- This script creates a table that makes sure id is not null

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT,
    name VARCHAR(256)
);
INSERT INTO id_not_null (id)
VALUE (1);
