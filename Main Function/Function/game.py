#!/usr/bin/env python3

# the first thing we will do is load any imports we may need

import requests
import pprint


# next we will ask the user for their name

name = input("Greetings Traveler, what is your name?")

response = input(f"Pick a Pokemon or item from the Pokeverse! ")

poke_char = "https://pokeapi.co/"

pokeresponse = requests.get(poke_char + response)

def hello():
    response = (f"Well hello {name} its so great to meet you. ")
    print(response)
hello()


def main():
# Ask user for input

# Decode the response
    poke_dj = pokeresponse.json()
    pprint.pprint(poke_dj)
    names = poke_dj.get('group')
    print("\nGreat Choice you chose:")
    for name in names:
        name_info = requests.get(name)
        print(name_info.json().get('name'))


main()
