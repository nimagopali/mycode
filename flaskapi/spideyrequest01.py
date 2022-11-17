#!/usr/bin/env python3
import requests
from pprint import pprint

URL= "http://127.0.0.1:2224/"

resp= requests.get(URL).json() # .json() gets the JSON from API and converts it to python data structure

pprint(resp)
