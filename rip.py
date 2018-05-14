# -*- coding: utf-8 -*-
"""
Created on Mon May 14 03:03:25 2018

@author: jlung20
"""

import json
import requests
import time
import string
import random

url = 'http://upe.42069.fun/WcDGr'
while(True):
    time.sleep(1)
    r = requests.get(url)
    try:
        print(r.json())
    except ValueError:
        pass
    #pyth = json.loads(r.text)
    #print(pyth['state'])
    time.sleep(1)
    lol = random.choice(string.ascii_lowercase)
    char = { 'guess' : lol }
    resp = requests.post(url, json=char)
    try:
        print(resp.json())
    except ValueError:
        pass 
'''while(True):
time.sleep(1)
resp = requests.post(url, json=char)
print(resp.json()) '''
#time.sleep(1)
#r = requests.get(url)
#print(r.json())