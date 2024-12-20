# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 16:42:55 2016

@author: ThinkPad
"""

'''
This program will calculate the area of a user selected shape. The current version is capable of performing these calculations on triangles and circles.
'''
#import non-standard modules
from math import pi
from time import sleep
from datetime import datetime
#create now variable 
now = datetime.now()
#welcome message
print "The Area Calculator is Loading"
#print current time
print "Current time: %s/%s/%s/ %s:%s" % (now.month, now.day, now.year, now.hour, now.minute)
#simulate thinking calculator
sleep(1)
#provide hint to user to input correct units
hint = "Don't forget to include the correct units! \nExiting..."

#prompt user input of shape
option = raw_input("Enter C for Circle or T for Triangle: ")

#allow for lowercase input by user
option = option.upper()

#calculate area of circle
if option == 'C':
    radius = float(raw_input("Enter radius: "))
    area = pi * radius**2
    print "The pie is baking..."
    sleep(1)
    print ("Area: %.2f. \n%s" % (area, hint))

#calculate area of triangle
elif option == 'T':
    base = float(raw_input("Enter base: "))
    height = float(raw_input("Enter height: "))
    area = (0.5) * base * height
    print "Uni Bi Tri..."
    sleep(1)
    print ("Area: %.2f. \n%s" %(area, hint))
  
#inform user input is invalid
else:
    print "You did not enter valid input! Good day!"