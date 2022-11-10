#!/usr/bin/env python3
"""Conditionals - rock, paper, scissors"""
import random

user_score = 0
computer_score = 0

print("==================================================")
print("***** START GAME *****")
print("==================================================")
print("<-- Let's play Rock, Paper, Scissors: Best of 5 -->")

while user_score < 3 and computer_score <3:
    user_input = input("\n*****Type a choice --> rock, paper, scissors:***** \n> ")
    random_choices = ["rock", "paper", "scissors"]
    computer_input = random.choice(random_choices)

    user_input = user_input.lower()
    computer_input  = computer_input.lower()
    print(f"You chose {user_input}! Computer chose {computer_input}!")

    if user_input == "paper" and computer_input == "rock":
        user_score += 1
        print(f"Congrats! You won this round!\nYour score = {user_score} \nComputer score = {computer_score}")
    elif user_input == "scissors" and computer_input == "paper":
        user_score += 1
        print(f"Congrats! You won this roundi!\n Your score = {user_score}\nComputer score = {computer_score}")
    elif user_input == "rock" and computer_input == "scissors":
        user_score += 1
        print(f"Congrats! You won this round!\nYour score = {user_score}\nComputer score = {computer_score}")
    elif computer_input == "paper" and user_input == "rock":
        computer_score += 1
        print(f"Computer won this round!\nYour score = {user_score}\nComputer score = {computer_score}")
    elif computer_input == "scissors" and user_input == "paper":
        computer_score += 1
        print(f"Computer won this round!\nYour score = {user_score}\nComputer score = {computer_score}")
    elif computer_input == "rock" and user_input == "scissors":
        computer_score += 1
        print(f"Computer won this round!\nYour score = {user_score}\nComputer score = {computer_score}")
    elif computer_input == user_input:
        print("It's a tie!")
        print(f"Your score = {user_score}")
        print(f"Computer score = {computer_score}")
    else:
         user_input
print("==================================================")
print("***** GAME OVER *****")
print("==================================================")




