#!/usr/bin/env python3
import wget

# imports always go at the top of your code
import requests

character= input("Choose your Pokemon: ").lower()
    
def main(char):
    try:
        pokeapi = requests.get(f"https://pokeapi.co/api/v2/pokemon/{char}").json()
        print(pokeapi)
        picurl= pokeapi["sprites"]["front_default"]
        wget.download(picurl, "/home/student/static/")
    except:
        print("That Pokemon does not exist")
main(character)
