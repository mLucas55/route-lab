# Introduction

A containerizable sql database with an accompanying CLI driver containing 17 queries for a guitar database.

# Description

This lab takes an existing SQL database and containerizes it in docker with the MySQL image. It contains a database, a Docker-compose file, a Python CLI driver, and a collection of query statements ranging from simple table selects, to slightly more complex inner-join and group-by statements that gather information about products, customers, orders, and more.

# Design

The Docker-compose file is written to use the MySQL image and initialize the guitar database within the container

The CLI driver is written in Python using mysql-connector-python and provides an interactive menu system for executing queries.

There are 7 simple single table queries
There are 5 inner join queries
There is 1 query with a function
There are 4 group by queries

# Running The Container & Driver

1. Download and install Docker on your machine, make sure it stays running in the background
2. Clone the Lab 7 folder to your machine and open it in your IDE of choice (VSCode recommended)
3. Open up a new terminal and CD to the working directory
4. Run the command: docker-compose up --build
5. Verify the container is running with the command: docker ps
6. Run the CLI driver with the command: docker exec -it lab7-python-app-1 python driver.py
7. Use the interactive menu to select and execute different types of queries