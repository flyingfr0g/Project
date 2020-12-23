import requests
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
    print((poke_name), ", which is classified as a: "),
    for t in type_info:
        print((t['type']['name']), "", sep=" type")
        if t['type']['name'] == "grass":
            print("grass types are weak against fire, bug, flying, ice, and poison types")

        if t['type']['name'] == "poison":
            print("poison types are weak against ground, and psychic types")

        if t['type']['name'] == "normal":
            print("normal types are weak against fighting, and ghost types")

        if t['type']['name'] == "bug":
            print("bug types are weak against fire, flying, and rock types")

        if t['type']['name'] == "electric":
            print("electric types are weak against ground types")

        if t['type']['name'] == "rock":
            print("rock types are weak against fighting, ground, steel, water and grass types")

        if t['type']['name'] == "dark":
            print("dark types are weak against bug, fighting, and fairy types")

        if t['type']['name'] == "fairy":
            print("fairy types are weak against poison, and steel types")

        if t['type']['name'] == "flying":
            print("bug types are weak against electric, ice, and water types")

        if t['type']['name'] == "ground":
            print("ground types are weak against grass, ice, and water types")

        if t['type']['name'] == "steel":
            print("steel types are weak against fire, fighting, and ground types")

        if t['type']['name'] == "dragon":
            print("dragon types are weak against dragon, ice, and fairy types")

        if t['type']['name'] == "fighting":
            print("fighting types are weak against fairy, flying, and psychic types")

        if t['type']['name'] == "ghost":
            print("ghost types are weak against ghost, and dark types")

        if t['type']['name'] == "ice":
            print("ice types are weak against fire, fighting, steel, and rock types")

        if t['type']['name'] == "water":
            print("water types are weak against electric, and grass types")

        if t['type']['name'] == "psychic":
            print("psychic types are weak against bug, dark, and ghost types")

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