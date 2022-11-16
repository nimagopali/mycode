#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""
"""
Significant changes:
1. Added Map Direction in showStatus() that describes every direction you can go from current room
2. Added Living room and item- knife
3. Added combat function where monster and player can fight until one of them dies
4. Added functionality to use inventory item(s) during the fight 
    a. if inventory has a knife as an item, it will be used as a weapon of choice for the player and doubles  player's damage to Monster
    b. Default weapon is set to 'hands'
5. The battle is automated until either Monster or Player dies
    a. The Battle report will be generated after each fight 
6. Created characters dictionary for different characters in the game, ex: Players & Monsters with different attributes like hp, damage and weapon
7. Added how many moves the player has made when using go [direction] command in the showStatus()
    
"""

import crayons
import random

"""

"""
def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    ## Added how to win and Map direction
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    To win:
        Get to the Garden with a key and a potion! Avoid the monsters!
        OR
        Get to the Kitchen to fight a Monster(Psst...get a knife first from the Living Room) 

    ''')
## count how many moves (get direction) player has made
countMove = 0
def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print(f'{crayons.red("---------------------------")}')
    print(f'{crayons.red("---------------------------")}')
    print('You are in the ' + currentRoom)
    ## print total move count to the every direction you can go
    print(f"Your total move count: {countMove}")
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
      print('---------------------------')
    

    ## iterate through key and value in order to describes every direction you can go from current room
      print("Map Direction:")
    for k, v in  rooms[currentRoom].items():
        if k != "item":
            print(f"Go {k} to enter  {v}")
    print(f'{crayons.red("---------------------------")}')
    print(f'{crayons.red("---------------------------")}')
    
def showBattleReport():
    """print the attributes like weapon, hp of player and monster"""
    print('---------------------------')
    print('B A T T L E  R E P O R T')
    print('---------------------------')
    print(f"Player's weapon:  { characters['Player']['weapon']}")
    print(f"Player's HP:      { characters['Player']['hp']}") 
    print(f"Monster's HP:     { characters['Monster']['hp']}")
    print('---------------------------')

def fight():
    """damage is randomized using random.randit for player and monster, and prints player's and monster's damage  and set the new HP for both  after damage"""
    playerDamage = random.randint(1, characters['Player']['damage'])
    monsterDamage = random.randint(1, characters['Monster']['damage'])
    
    print(f'Played attacked Monster with: {playerDamage}')
    print(f'Monster attacked Player with: {monsterDamage}')

    characters['Player']['hp'] = characters['Player']['hp'] - monsterDamage
    characters['Monster']['hp'] = characters['Monster']['hp'] - playerDamage
  

def combat():
    """automatically fights once player input yes to fight until one wins. If player says no to fight, player dies"""
    print('A monster has appeared!')
    showBattleReport()

    combat_start = True

    while combat_start:
        fight_start = False

        choice = input('Do you want to fight? Yes or No\n>')
        choice.lower()

        if choice == 'yes':
            fight_start = True

        elif choice == 'no':
            print('A monster has got you... GAME OVER!')
            break
        
        while fight_start: 
            fight()
            showBattleReport()

            if characters['Monster']['hp'] <= 0:
                print('You win, thanks for saving the world!')
                combat_start = False
                break

            elif characters['Player']['hp'] <= 0:
                print('You died, better luck next time')
                combat_start = False
                break


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'west'  : 'Living Room',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion'
               },
            'Garden' : {
                  'north' : 'Dining Room'
            },
            'Living Room'  : {
                    'east' : 'Hall',
                    'item' : 'knife'
                }
         }

## dictionary for characters( health, damage, weapon)
characters ={
        'Player':{
            'hp' : 200,
            'damage': 20,
            'weapon' : 'hands'
            },
        'Monster':{
            'hp':200,
            'damage':30
            }
        }

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

## breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
            countMove+=1
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')

            ## If the item is 'knife', choose it as the Player's weapon of choice
            ## Default weapon is set to 'hands'
            if 'knife' == move[1]:
                characters['Player']['weapon'] = 'knife'
                characters['Player']['damage'] *= 2 

            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    ## If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        combat()
        break
    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print(f"{crayons.red('You escaped the house with the ultra rare key and magic potion... YOU WIN!')}")
        break

