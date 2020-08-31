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
    for c in character_dict:
        if (c['homeworld']):
            del c['homeworld']
        if (c['films']):
            del c['films']
        if (c['species']):
            del c['species']
        if (c['vehicles']):
            del c['vehicles']
        if (c['starship']):
            del c['starship']
    convert_height(float(character_dict['height']))
    convert_weight(float(character_dict['mass']))
    return character_dict

def transform_planet(planet_dict):
    # Clean up cross-referencing data
    for p in planet_dict:
        if (p['residents']):
            del p['residents']
        if (p['films']):
            del p['films']
    return planet_dict

def transform_starship(starship_dict):
    # Clean up cross-referencing data
    for s in starship_dict:
        if (s['pilots']):
            del s['pilots']
        if (s['films']):
            del p['films']
    return starship_dict

def transform_vehicle(vehicle_dict):
    # Clean up cross-referencing data
    for v in vehicle_dict:
        if (v['pilots']):
            del v['pilots']
        if (v['films']):
            del v['films']
    return vehicle_dict

def transform_species(species_dict):
    # Clean up cross-referencing data
    for s in species_dict:
        if (s['people']):
            del s['people']
        if (s['films']):
            del s['films']
    return species_dict  

def convert_height(height):
    return (height / 2.54)

def convert_weight(weight):
    return (weight * 2.205)

film_json = requests.get(f"http://swapi.dev/api/films/{film_num}/").json()
film_dict = json.loads(film_json)

characters_list = film_json.get('characters')
planets_list = film_json.get('planets')
starships_list = film_json.get('starships')
vehicles_list = film_json.get('vehicles')
species_list = film_json.get('species')

for character in characters_list:
    character_json = requests.get(character).json()
    character_dict = json.loads(character_json)
    master_character_dict.update(transform_char(character_dict))

for planet in planets_list:
    planet_json = requests.get(planet).json()
    planet_dict = json.loads(planet_json)
    master_planet_dict.update(transform_planet(planet_dict))

for starship in starships_list:
    starship_json = requests.get(starship).json()
    starship_dict = json.loads(starship_json)
    master_starship_dict.update(transform_starship(starship_dict))

for vehicle in vehicles_list:
    vehicle_json = requests.get(vehicle).json()
    vehicle_dict = json.loads(vehicle_json)
    master_vehicle_dict.update(transform_vehicle(vehicle_dict))

for species in species_list:
    species_json = requests.get(species).json()
    species_dict = json.loads(species_json)
    master_species_dict.update(transform_species(species_dict))

film_dict['characters'] = master_character_dict
film_dict['planets'] = master_planets_dict
film_dict['starships'] = master_starships_dict
film_dict['vehicles'] = master_vehicles_dict
film_dict['species'] = master_species_dict

final_json = json.dumps(film_dict)
with open('task_two.json', 'w') as outfile:
    json.dump(final_json, outfile)
