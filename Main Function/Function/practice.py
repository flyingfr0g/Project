#!/usr/bin/env python3

import

def main():
    poke_base_uri = "pb"
    # Ask user for name
    player_name = input("Greetings Traveler, what is your name? ")
    print(f"Well hello, {player_name}, its so great to meet you. Welcome to my Pokedex ")
    poke_choice = input("Please type in the name of the Pokemon you wish to learn about:  ")
    pokeresponse = requests.get(f"{poke_base_uri}{poke_choice}/")
    pprint.pprint(pokeresponse)
    # Decode the response
    #poke_choice = (pokeresponse)
    #pprint.pprint(poke_choice)
    #names = poke_choice.get('name')
    #print("\nGreat Choice you chose:")
    #for     name in names:
    #name_info = requests.get(name)
    #print(name_info.json().get('name'))


main()
