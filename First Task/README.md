# First Task
## Requirements
 - Develop a server which is connected with 3 MongoDB instances using different types of database host: local db, local db via docker container, web db.
 - Make up `POST` endpoint for addition documents into all databases.
 - Make up `DELETE` endpoint for removal documents from all databases.
 - Make up generator for documents.
 - Measure query execution time.
## Settings
- Local MongoDB on port 27017.
- Local docker MongoDB container on port 27001. Ran by command `docker run --name mongodb -d -p 27001:27017 mongo`.
- Web MongoDB Atlas.
- Connected to db using `pymongo` python package.
- Collection `Clients`:

| First name | Second name | Age | Gender | Phone | Country | Occupation | Education |
| ---------- | ----------- | --- | ------ | ----- | ------- | ---------- | --------- |
|            |             |     |        |       |         |            |           |
- Fields first_name, second_name, country, occupation, education are chosen from the given list of values presented in `seed.py`.
- Fields age, gender, phone are generated using `random` python package.
- Local server is built using `Flask` on port 5000.
- Local variable `size` describing number of documents for addition (used 1000).
## Description
Firstly, server initialize databases by adding 1 document into each (`fill_up` function). This is made to create collection in each db in order not to include this setting up time in final measurement. The server has endpoint `\eval` with two methods: `POST` for adding `size` documents into all databases and `DELETE` for removal all documents from collection (`make_move` function for each db).

It is used `time` python package to measure execution time. Function `eval` returns 3 time measurement in seconds for each type of connection.

## Visualization
