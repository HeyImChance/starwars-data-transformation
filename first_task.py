"""Retrieve data from Star Wars API and insert into MySQL

This script will create a list of 15 random values between 1 and 83
(which is the current range of Star Wars character IDs on swapi.dev),
retrieve and insert relevant data into a MySQL database.
"""

import requests
import re
import random
import json
import os
import mysql.connector
from mysql.connector import Error

# Ensure environment variables are set to avoid hard-coding or passing args to CLI
if ('SWAPI_USER' not in os.environ) or ('SWAPI_PASS' not in os.environ):
    print('You must define DB creds SWAPI_USER and SWAPI_PASS')
    sys.exit(1)

# Instantiate MySQL connection to localhost
mydb = mysql.connector.connect(
    host='localhost',
    user=os.environ.get('SWAPI_USER'),
    password=os.environ.get('SWAPI_PASS'),
    database='swapi_data'
)

# Will contain master list of all films seen during character / film retrieval
master_film_list = []

# Retrieves and filters SWAPI JSON data and inserts into MySQL database
def filter_chars_insert():
    # Using random.sample() to generate character ID list
    randvals = random.sample(range(1, 83), 15)

    mysql_insert = "INSERT INTO characters(name, films, char_num) VALUES({}, {}, {})"

    print('Inserting characters...')
    for char_id in randvals:
        # Get JSON for character at char_id
        person_json = requests.get(f"http://swapi.dev/api/people/{char_id}/").json()
        name = str(person_json.get('name'))
        # Get list of cross-referenced film URLs
        films_list = person_json.get('films')
        if films_list is None:
            films_list = []
        film_names = []
        # Retrieve film names from films endpoint using URLS
        for film in films_list:
            title = requests.get(film).json().get('title')
            if title not in master_film_list:
                master_film_list.append(str(title))
            film_names.append(title)   
        films = str(film_names).strip('[]')
        # Try / catch to see any insertion errors along the way
        try:
            cursor = mydb.cursor()
            cursor.execute(mysql_insert.format("\"" + name + "\"", "\"" + films + "\"", char_id))
            mydb.commit()
            cursor.close()
        except mysql.connector.Error as error:
            print("Failed to insert record into characters table {}".format(error))

def return_filtered_json():
    master_dict = {}
    chars_per_film = "SELECT name FROM characters WHERE films like '%{}%'"
    print("Getting list of names per film...")
    for film in master_film_list:
        try:
            cursor = mydb.cursor()
            final_statement = chars_per_film.format(film)

            cursor.execute(final_statement)
            result = cursor.fetchall()
            master_dict[film]=result
        except mysql.connector.Error as error:
            print('Failed to retrieve records from table {}'.format(error))
    print(json.dumps(master_dict, indent=2))
    
filter_chars_insert()
return_filtered_json()








