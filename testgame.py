#!/usr/bin/env python3

import requests
from random import randint

## Add Riddles: use pokemon API to ask the user guess what pokemon am I


# riddle function: use a function with the return value
# when user successful solve the riddle, return 2
# if user fails to solve, return 3
# use more if statements in the main loop to check win/lose
def riddle():
    API = "https://pokeapi.co/api/v2/pokemon/" 
    pokemon=requests.get(API+str(randint(1,12))).json()
    # print(pokemon['name'])
    # print(pokemon['types'][0]['type'])

    guess=1

    print("Welcome to the Pokemon Riddle!")
    print("Guess what Pokemon am I?")
    while True:
        if guess==1:
            print(f"My type is {pokemon['types'][0]['type']['name']}.")
        elif guess==2:
            print(f"My ability is {pokemon['abilities'][0]['ability']['name']}.")
        elif guess==3:
            print(f"My pokedex ID is {pokemon['id']}")
        else:
            return 2
        user_input=input("Your guess is >> ").lower()
        if user_input == pokemon['name']:
            print("Congratz! That is correct")
            return 3
        guess+=1

## count how many "moves" the player has made
move_count=0

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    ''')
    print('Get to the Garden with a key and a potion to win! Avoid the monsters! Commands include go direction and get item.')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there is an item in the room, if so, print it
    if "item" in rooms[currentRoom]:
        print('You see a '+ rooms[currentRoom]['item'])
    print("---------------------------")

# player's inventory
inventory=[]

# a dictionary links a room to other rooms
rooms ={
        'Hall':
            {
                'south':'Kitchen',
                'east':'Dining Room',
                'item':'key'
            },
        'Kitchen':
            {
                'north':'Hall',
                'item':'monster'
            },
        'Dining Room':
            {
                'west':'Hall',
                'south':'Garden',
                'east':'Basement',
                'item':'potion'
            },
        'Garden':
            {
                'north':'Dining Room'
            },
        'Basement':
            {
                'west':'Dining Room',
                'east':'Backyard',
                'item':'wooden stick'
            },
        'Backyard':
            {
                'west':'Basement',
                'item':'zombie'
            }
        }

# start the player in the hall
currentRoom='Hall'

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # The player must type something in
    # otherwise input will keep asking
    move=""
    while move == '':
        move=input('>')

    # normalizing input:
    move=move.lower().split(" ", 1) # ["go","south"] ["get","key"]

    # if user types 'go' first
    if move[0] == 'go':
        # check that they are allowed whereever they want to go
        if move[1] in rooms[currentRoom]:
            # success: change the currentroom to the new room
            currentRoom = rooms[currentRoom][move[1]]
            move_count+=1
        else:
            print('You can\'t go that way!')
    
    # if user types 'get' first
    if move[0]=='get':
        # make 2 checks
        # 1. if the current room contains an item
        # 2. if the item in the room matches the user input "get ITEM"
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory.append(move[1])
            print(move[1]+' got!')
            # delete the item KV pair from the room's dict
            del rooms[currentRoom]['item']
        # if there is no item in the room, or the item does not match user's input
        else:
            print("Cannot get "+move[1]+" in the "+currentRoom+"!")
    # define winning condition (to break the while loop)
    if currentRoom=='Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

    # change 1: added 2 more rooms with items, as well as a gameover condition
    elif currentRoom=='Backyard' and 'item' in rooms['Backyard']:
        # if player has a wooden stick, player will kill the zombie. Otherwise, gameover
        print('A zombie spotted you!')
        if 'wooden stick' in inventory:
            print("You stabbed the zombie's head with your wooden stick. The zombie struggled but eventfully stopped moving.")
            # remove wooden stick from your inventory
            inventory.remove('wooden stick')
            # remove zombie from the backyard
            del rooms['Backyard']['item']
            continue
        else:
            # gameover
            print("You thought:\'I should have grabbed the stick from the basement...\'. You puched the zombie's head but nothing happened. Better luck next time.")
            break
    
    # change 3: added a pokemon riddle for Dining room
    elif currentRoom=='Dining Room':
        print("You hear a very rusty wheel noise coming from a little man wearing a mask, he says: ")
        print("Let's play a game.")
        print("=================")
        riddle()
        if riddle()==2:
            print('You failed the riddle. The tile under your feet suddenly disappeared. You fell into the abyss.')
            break
        else:
            continue
    # change 2: count the move steps: simulating time
    # if move_count>=10: player gets killed
    if move_count<5:
        print('You can still see a little bit of sunlight, but you might want to hurry up and find a way out...')
    elif move_count>=5 and move_count<10:
        print('It is getting darker and darker. You start to hear creepy noises. ')
    else:
        print('Now it is completely dark. A monster jumps out and bites you on the neck. Better luck next time.')
        break
