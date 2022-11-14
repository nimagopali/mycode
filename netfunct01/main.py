#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

# python3 -m pip install crayons
import crayons
import json

# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys(): # looping through the dict
        print(f'Handshaking. .. ... connecting with {ip}') # fstring
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            print(f'Attempting to sending command --> {mycmds}')
            # we'll learn to write code that sends cmds to device here
    return None

#Create a second function, devicereboot. It should accept a list of IPs as a single argument. The function should iterate through the list IPs, and for each one, print, "Connecting to.. ", then print, "REBOOTING NOW!". Be sure to comment your code.
def devicereboot(IPslist):
    for ip in IPslist:
        print(f"Connecting to.. {ip}, REBOOTING NOW!")

# start our main script
def main():
    """called at runtime"""

    # dict containing IPs mapped to a list of physical interfaces and their state
    #devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1": ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}
    
    with open("devicecmd.json", "r") as devicecmdfile:
        # need to import json lib
        # json.load(filename): takes a file obj and returns the json obj
        devicecmd = json.load(devicecmdfile) # decode the JSON from the file to pythonic data

    print("Welcome to the network device command pusher") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(devicecmd) # call function to push commands to devices
    devicereboot(devicecmd)

# call our main function
main()

