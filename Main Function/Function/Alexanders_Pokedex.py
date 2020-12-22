#!/usr/bin/env python3

# the first thing we will do is load any imports we may need

import requests
import pprint

# Ask user for name
def greeting():
    player_name = input("Greetings Traveler, what is your name? ")
    print(f"Well hello, {player_name}, its so great to meet you. Welcome to my Pokedex ")

# Next is our main function

def pokedex():
    poke_base_uri = "https://pokeapi.co/api/v2/pokemon/"
    poke_choice = input("Please type in the name of the Pokemon you wish to learn about or choose"
                        " a random number between 1 and 898:  ")
    pokeresponse = requests.get(f"{poke_base_uri}{poke_choice}/")

    # Decode the response

    poke = pokeresponse.json()
    print("Great Choice you chose:")
    name_info = poke.get("species")
    type_info = poke.get('types')
    abilities_info = poke.get('abilities')
    poke_name = (name_info['name'])
    print((poke_name), ": which is classified as a: "),
    for t in type_info:
        print((t['type']['name']), "", sep=" type")
    print( "this Pokemon's signature abilities are: ")
    for a in abilities_info:
            print((a['ability']['name']),"", sep=",")



def close_pokedex():
    print ("Thank you for using Alexander's Pokedex, look forward to updates!")
    quit()


# run our greeting function
greeting()


## run our main function
pokedex()

#ask the user if they are finished and terminate
while True:
    zzz = input('Would you like to look up another Pokemon? y/n : ')
    if zzz.lower().startswith("y"):
        pokedex()
    elif zzz.lower().startswith("n"):
        close_pokedex()
    else:
        print("sorry I did not understand your input")