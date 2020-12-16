#!/usr/bin/env python3

# the first thing we will do is load any imports we may need

import urllib.request
import requests
import pprint
import json

# next we will ask the user for their name and set it as a variable

name = input("Greetings Traveler, what is your name?")

# next we will set some other variables

response = input(f"Pick a Pokemon or item from the Pokeverse! ")

poke_char = "https://pokeapi.co/api/v2/{endpoint}/"

pokeresponse = requests.get(poke_char + response)

def hello():
    response = (f"Well hello {name} its so great to meet you. ")
    print(response)
hello()

# Next is our main function

def main():

# Decode the response
    poke_dj = pokeresponse.json()
    pprint.pprint(poke_dj)
    names = poke_dj.get('name')
    print("\nGreat Choice you chose:")
    for name in names:
        name_info = requests.get(name)
        print(name_info.json().get('name'))


main()
