"""Retrieve film data from Star Wars API and output JSON file.

This script will pull and transform character, planet, starship and species data
for the Star Wars film 'A New Hope' and place it in a JSON file.
"""

import requests
import json
import sys

# Made it so this script is capable of getting any film data offered by SWAPI.
film_input = input("Enter a film number 1-6: ")
try:
    film_num = int(film_input)
except ValueError:
    print("Please enter an integer value")

if (film_num <=0 or film_num > 6):
    sys.exit("Please enter a number between 1 and 6")

# These will be assembled into master dict after each dict is assembled
master_character_dict = {}
master_planets_dict = {}
master_starships_dict = {}
master_vehicles_dict = {}
master_species_dict = {}

# Take in json, extract all data that doesn't cross-reference
def transform_char(character_dict):
    # Clean up cross-referencing data
    if 'homeworld' in character_dict:
        del character_dict['homeworld']
    if 'films' in character_dict:
        del character_dict['films']
    if 'species' in character_dict:
        del character_dict['species']
    if 'vehicles' in character_dict:
        del character_dict['vehicles']
    if 'starships' in character_dict:
        del character_dict['starships']
    if character_dict['height'] == 'unknown':
        character_dict['height'] = 0
    # Mass values are potentially in the 1000s
    if ',' in character_dict['mass']:
        character_dict['mass'] = character_dict['mass'].replace(',','')
    if character_dict['mass'] == 'unknown':
        character_dict['mass'] = 0
    convert_height(float(character_dict['height']))
    convert_weight(float(character_dict['mass']))
    return character_dict

def transform_planet(planet_dict):
    # Clean up cross-referencing data
    if 'residents' in planet_dict:
        del planet_dict['residents']
    if 'films' in planet_dict:
        del planet_dict['films']
    return planet_dict

def transform_starship(starship_dict):
    # Clean up cross-referencing data
    if 'pilots' in starship_dict:
        del starship_dict['pilots']
    if 'films' in starship_dict:
        del starship_dict['films']
    return starship_dict

def transform_vehicle(vehicle_dict):
    # Clean up cross-referencing data
    if 'pilots' in vehicle_dict:
        del vehicle_dict['pilots']
    if 'films' in vehicle_dict:
        del vehicle_dict['films']
    return vehicle_dict

def transform_species(species_dict):
    # Clean up cross-referencing data
    if 'people' in species_dict:
        del species_dict['people']
    if 'films' in species_dict:
        del species_dict['films']
    return species_dict  

def convert_height(height):
    return (height / 2.54)

def convert_weight(weight):
    return (weight * 2.205)

film_json = requests.get(f"http://swapi.dev/api/films/{film_num}/").json()

characters_list = film_json.get('characters')
planets_list = film_json.get('planets')
starships_list = film_json.get('starships')
vehicles_list = film_json.get('vehicles')
species_list = film_json.get('species')

for character in characters_list:
    character_json = requests.get(character).json()
    master_character_dict.update(transform_char(character_json))

for planet in planets_list:
    planet_json = requests.get(planet).json()
    master_planets_dict.update(transform_planet(planet_json))

for starship in starships_list:
    starship_json = requests.get(starship).json()
    master_starships_dict.update(transform_starship(starship_json))

for vehicle in vehicles_list:
    vehicle_json = requests.get(vehicle).json()
    master_vehicles_dict.update(transform_vehicle(vehicle_json))

for species in species_list:
    species_json = requests.get(species).json()
    master_species_dict.update(transform_species(species_json))

film_json['characters'] = master_character_dict
film_json['planets'] = master_planets_dict
film_json['starships'] = master_starships_dict
film_json['vehicles'] = master_vehicles_dict
film_json['species'] = master_species_dict

final_json = json.dumps(film_json)
with open('task_two.json', 'w', indent=4) as outfile:
    json.dump(final_json, outfile)
