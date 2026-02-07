-- Creates the table unique_id
-- id INT with default value 1 and must be unique, name VARCHAR(256)
-- The database name will be passed as an argument of the mysql command

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
