-- Creates the database hbtn_0d_usa and the table cities
-- id INT: unique, auto generated, not null, primary key
-- state_id INT: not null, foreign key referencing states(id)
-- name VARCHAR(256): not null

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database
USE hbtn_0d_usa;

-- Create the table cities
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
