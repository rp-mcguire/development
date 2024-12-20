# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:52:51 2020

@author: raypm
"""

import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'

number = input("Number of passwords_ - ")
number = int(number)

length = input("Password length? - ")
length = int(length)

for p in range(number):
    password = " "
    for c in range(length) :
        password += random.choice(chars)
    print(password)