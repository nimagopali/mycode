#!/usr/bin/env python3

#only import the call and check_output functions from the subprocess module.
from subprocess import call

call(["ip", "link", "show", "up"])
print("This program will check your interfaces.")

interface = input("Enter an interface, like, ens3: ")

call(["ip", "addr", "show", "dev", interface])

call(["ip", "route", "show", "dev", interface])



