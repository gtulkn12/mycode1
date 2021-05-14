#!/usr/bin/env python3
import requests
url= "https://pokeapi.co/api/v2/pokemon/pikachu"

resp= requests.get(url)
pokedex= resp.json()




#print(dir(resp))
#print(resp.json())
#print(type(resp.json()))
