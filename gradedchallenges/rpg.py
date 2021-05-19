#!/usr/bin/python3

from typing import ItemsView

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
          for thing in rooms[currentRoom]['item']:
                  result= rooms[currentRoom]['item'][thing]
                  print(f'You see a {result}')
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

        'Hall' : {
                'description' : 'You are in the Hall, you have a door to your South, East',                
                'east' : 'Dining Room',
                'south' : 'Kitchen',
                'west' : 'Basement',
#CHALLENGE - Added an item decription w/ a dictionary
                'item'  : {'key' : 'Shiny Golden Key on a table in the corner',
                           'sword': 'Golden Sword hanging on the wall'}
        },
        'Kitchen' : {
                'description' : 'You are in the Kitchen, you have a door to your North',
                'north' : 'Hall',
                'south' : 'Dungeon',
                'item'  : {'monster' : 'Big Scary Cookie Monster'}
        },
        'Dining Room' : {
                'description' : 'You are in the Dinning Room, you have a door to your West, East and North',                               
                'north' : 'Pantry',
                'east': 'Garden',
                'west' : 'Hall',
                'item' : {'potion' : 'Shiny bottle of green potion'}
        },
#CHALLENGE - Added Basement as additional Room to the west of Hall
        'Basement' : {
                'description' : 'You are in the Basement, you have doors to your East and South',
                'east' : 'Hall',
                'south' : 'Dungeon',
                'item' : {'cookie' : 'Oreo Cookie'}
        },
        'Garden' : {
                'description' : 'You are in the Garden, you have a door to your North',
                'west' : 'Dining Room'
        },
        'Pantry' : {
                'description' : 'You are in the Pantry, you have a door to your South',
                'south' : 'Dining Room',
                'item' : {'cookie' : 'Chocolate Chip Cookie'}
        },
#CHALLENGE - added TrapDoor from Kitachen into Living Room, Can only enter living through trapdoor and only exit to dinning room
        'Dungeon' : {
                'description' : 'You went through a TRAP-Door that landed you in the Dungeon, you have a door to your East',
                'east' : 'Dining Room'
        }            
}

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
      print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break