#!/usr/bin/env python3
import requests
from pprint import pprint

URL= "http://127.0.0.1:2224/data"
#send a GET request to your Flask API; it should target the endpoint that returns JSON
#take the returned JSON and "normalize" it into a format that is easy for users to understand.
resp= requests.get(URL).json()

pprint(resp)
