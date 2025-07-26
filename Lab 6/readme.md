# Introduction

A containerizable sql database with an accompanying SQL script containing 17 queries for a guitar database.

# Description

This lab is takes an existing SQL database and containerizes it in docker with the MySQL image. It contains a database, a Docker-compose file and a collection of query statements ranging from simple table selects, to slightly more complex inner-join and group-by statements that gather information about products, customers, orders, and more.

# Design

The Docker-compose file is written to use the MySQL image and initilize the guitar database within the container

The SQL scripts are written in SQL using DBeaver and is intended to be used with the MySQl guitar database.

There are 7 simple single table queries
There are 5 innjer join queries
There is 1 query with a function
There are 4 group by queries

# Running The Script (DBeaver)

1. Download and install Docker on your machine, make sure it stays running in the background
2. Clone the Lab 6 folder to your machine and open it in your ID of choice (VSCode recommended)
3. Open up a new terminal and CD to the working directory
4. Run the command: docker-compose up-d
5. Verify the container is running with the command: docker ps
6. Connect to MySQL inside the container with the command: docker exec -it mysql_db mysql -u root -p
7. Enter the defined passowrd
8. Enter the command: USE my_guitar_shop;
9. Enjoy using the queries from script.sql, or your own new quieries!