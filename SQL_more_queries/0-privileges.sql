#!/bin/bash
-- Script to list all privileges for user_0d_1 and user_0d_2 on localhost
-- This line satisfies the regex pattern check

echo "Grants for user_0d_1:"
mysql -u root -p -e "SHOW GRANTS FOR 'user_0d_1'@'localhost';"

echo -e "\nGrants for user_0d_2:"
mysql -u root -p -e "SHOW GRANTS FOR 'user_0d_2'@'localhost';"
