#!/usr/bin/env python3


user_input =int(input("How many bottles of beet you're couting down from!"))

if user_input<=100:
    for item in range(user_input):
        print(f'''{user_input} bottles of beer on the wall!\n{user_input} bottles of beer on the wall!{user_input}bottles of beer! You take one down, pass it around!\n98 bottles of beer on the wall! 98 bottles of beer on the wall! 98 bottles of beer! You take one down, pass it around!97 bottles of beer on the wall! 97 bottles of beer on the wall! 97 bottles of beer! You take one down, pass it around!''')
        
