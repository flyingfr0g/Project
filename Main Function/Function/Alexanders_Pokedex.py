#!/usr/bin/env python3

# the first thing we will do is load any imports we may need

import urllib.request
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
    poke_ch = pokeresponse.json()
    pprint.pprint(poke_ch)
    names = poke_choice.get('name')
    print("\nGreat Choice you chose:")
    for     name in names:
        name_info = requests.get(name)
        print(name_info.json().get('name'))


main()