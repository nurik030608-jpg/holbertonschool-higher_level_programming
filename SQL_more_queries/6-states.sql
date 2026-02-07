-- Creates the database hbtn_0d_usa and the table states
-- id INT: unique, auto generated, not null, primary key
-- name VARCHAR(256): not null

-- Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database
USE hbtn_0d_usa;

-- Create the table
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
