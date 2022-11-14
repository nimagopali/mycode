#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

# Write a for loop that returns all the animals from the NE Farm!
for item in farms:
    if item["name"] == "NE Farm":
        print(item["agriculture"])

#  Ask a user to choose a farm (NE Farm, W Farm, or SE Farm). Return the plants/animals that are raised on that farm.
user_input = input("Choose a farm (NE Farm, W Farm, or SE Farm)")

for item in farms:
    if item["name"].lower() == user_input.lower():
        print(item["agriculture"])

# Ask a user to choose a farm (NE Farm, W Farm, or SE Farm)... but only return ANIMALS from that particular farm
user_input = input("Choose a farm(NE Farm, W Farm, or SE Farm)")

plants = ["carrots", "celery"]

for farm in farms:
    if item["name"].lower() == user_input.lower():
        for animal in farm["agriculture"]:
            if animal not in plants:
                print(animal)

