# -*- coding: utf-8 -*-
"""
Created on Mon May 14 03:03:25 2018

@author: jlung20
"""

import requests
import time
import string
import random

url = 'http://upe.42069.fun/WcDGr'

# continues guessing ad infinitum
while(True):
    # sleep to not overload the service
    time.sleep(1)
    r = requests.get(url)
    # print to get status of game
    try:
        print(r.json())
    # in the case that there's a JSONDecodeError
    except ValueError:
        pass
    
    # sleep to not overload the service
    time.sleep(1)
    rand_char = random.choice(string.ascii_lowercase)
    guess = { 'guess' : rand_char }
    resp = requests.post(url, json=guess)
    # print to get status of game
    try:
        print(resp.json())
    # in the case that there's a JSONDecodeError
    except ValueError:
        pass 
    
