#!/bin/bash

# Script to list all privileges for user_0d_1 and user_0d_2 on localhost

# Display grants for user_0d_1
echo "Grants for user_0d_1:"
mysql -u root -p -e "SHOW GRANTS FOR 'user_0d_1'@'localhost';"

# Display grants for user_0d_2
echo -e "\nGrants for user_0d_2:"
mysql -u root -p -e "SHOW GRANTS FOR 'user_0d_2'@'localhost';"
