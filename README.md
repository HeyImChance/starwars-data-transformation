# starwars-data-transformation


This project pulls data from the Star Wars API (swapi.dev), transforms it, and places it in a local MySQL database for retrieval.

# Dependencies

* Python 3
* Python MySQL connector (`pip install mysql-connector-python`)
* Local MySQL 8.0 setup (more detail below)

# MySQL Setup

* Make sure local mysqld is running on localhost (or edit host value in `first_task.py` to match your setup)
* Run SQL contained in swapi_data_characters.sql
* Grant privileges on swapi_data schema to user of your choice
* Export that user's details to `SWAPI_USER` and `SWAPI_PASS`
* If you wish to re-run first_task.py, truncate characters table (there is a uniqueness constraint on character number field)

NOTE: MySQL file contained here will insert example data generated by `first_task.py`. You can feel free to truncate this and start fresh.
