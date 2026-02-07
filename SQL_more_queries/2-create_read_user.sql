-- Creates the database hbtn_0d_2 and the user user_0d_2
-- user_0d_2 has only SELECT privilege in the database hbtn_0d_2

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user if it doesn't exist and set the password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant only SELECT privilege on the specific database to the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush privileges to ensure the changes take effect immediately
FLUSH PRIVILEGES;
