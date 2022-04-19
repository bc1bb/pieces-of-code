#!/usr/bin/env bash
# MariaHelper (github:jusdepatate/pieces-of-code:/mariahelper.sh)

if [ "$EUID" -ne 0 ]; then
    echo "Please, execute as root."
    exit 1
fi

if [ "$1" = "" ]; then
    # in case of no argument
    echo "createuser - Create a user with(out) a db"
    echo "createroot - Create a root-like user"
    echo "deleteuser - Delete user"
    echo "listuser - List all users"
    echo "createdb - Create a db"
    echo "deletedb - Delete a db"
    echo "listdb - List all db"
    echo ""

    printf "\033[1mWhat do you want to do ?\033[0m " && read -r whattodo
    echo ""

else
    # in case of argument
    whattodo="$1"
fi

if [ "$whattodo" = "createuser" ]; then
    printf "What is the name of the user ? " && read -r username
    printf "What is the password of the user ? " && read -r password
    printf "Do you want a db with the user ? (y/n) " && read -r yndb

    if [ "$yndb" = "y" ]; then
         # create user with db
        echo "CREATE USER $username@'localhost' IDENTIFIED BY '$password';" \
             "CREATE DATABASE IF NOT EXISTS $username;" \
             "GRANT ALL PRIVILEGES ON $username.* TO $username@'localhost';" \
             "FLUSH PRIVILEGES;" | mysql

    else
        # create user without db
        echo "CREATE USER $username@'localhost' IDENTIFIED BY '$password';" \
             "FLUSH PRIVILEGES;" | mysql
    fi
elif [ "$whattodo" = "createroot" ]; then
    # create a root-like user
    printf "What is the name of the root-like user ? " && read username
    printf "What is the password of the user ? " && read password
    echo "CREATE USER $username@'localhost' IDENTIFIED BY '$password';" \
         "GRANT ALL PRIVILEGES ON  *.* to $username@'localhost' WITH GRANT OPTION;" \
         "FLUSH PRIVILEGES;" | mysql

elif [ "$whattodo" = "deleteuser" ]; then
    # delete a user
    printf "What is the name of the user to be deleted ? " && read username
    echo "REVOKE ALL PRIVILEGES, GRANT OPTION FROM $username@'localhost';" \
         "DROP USER IF EXISTS $username@'localhost';" \
         "FLUSH PRIVILEGES;" | mysql

elif [ "$whattodo" = "listuser" ]; then
    # list existing users
    echo "SELECT User FROM mysql.user;" | mysql

elif [ "$whattodo" = "createdb" ]; then
    # create databse
    printf "What is the name of the db ? " && read -r db
    echo "CREATE DATABASE IF NOT EXISTS $db;" | mysql

elif [ "$whattodo" = "deletedb" ]; then
    # delete database
    printf "What is the name of the db to be deleted ? " && read -r db
    echo "DROP DATABASE $db;" | mysql

elif [ "$whattodo" = "listdb" ]; then
    # list databases
    echo "SHOW DATABASES;" | mysql

else
    echo "No command recognized."
    exit 1
fi