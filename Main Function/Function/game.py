#!/usr/bin/env python3

# the first thing we will do is load any imports we may need

import urllib.request
import pprint
import requests
import json


# Next is our main function

def main():
    poke_base_uri = "https://pokeapi.co/api/v2/ability/"
    # Ask user for name
    player_name = input("Greetings Traveler, what is your name? ")
    print(f"Well hello, {player_name}, its so great to meet you. ")
    poke_choice = input("Pick a Pokemon to lookup. ")
    pokeresponse = requests.get(f"{poke_base_uri}{poke_choice}/")
    print(pokeresponse)
    # Decode the response
    # poke_dj = pokeresponse.json()
    # pprint.pprint(poke_dj)
    # names = poke_dj.get('name')
    # print("\nGreat Choice you chose:")
    # for name in names:
    #    name_info = requests.get(name)
    #    print(name_info.json().get('name'))


main()