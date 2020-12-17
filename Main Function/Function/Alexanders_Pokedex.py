#!/usr/bin/env python3

# the first thing we will do is load any imports we may need

import urllib.parse
import pprint
import requests
import json


# Next is our main function

def main():
    poke_base_uri = "https://pokeapi.co/api/v2/pokemon/"
    # Ask user for name
    player_name = input("Greetings Traveler, what is your name? ")
    print(f"Well hello, {player_name}, its so great to meet you. Welcome to my Pokedex ")
    poke_choice = input("Please type in the name of the Pokemon you wish to learn about:  ")
    pokeresponse = requests.get(f"{poke_base_uri}{poke_choice}/")

    # Decode the response
    poke = pokeresponse.json()
    print("Great Choice you chose:")
    name_info = poke.get("species")
    type_info = poke.get("types")
    ability_info = poke.get("abilities")
    pprint.pprint(name_info['name'])
    pprint.pprint(type_info)
    pprint.pprint(ability_info[{'ability'}])

main()