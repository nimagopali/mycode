#!/usr/bin/env python3

import requests

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

   # print(pokeapi)
    
    sliced =  pokeapi["sprites"]["front_default"]
    print(sliced)

    # Part 2- Slicing WITH a for loop!
    pokemonNameMove = pokeapi["moves"]
    print(pokemonNameMove)
    for x in pokemonNameMove:
       print( x["move"]["name"])

main()

