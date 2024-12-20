# -*- coding: utf-8 -*-
"""
This is a rudementary trip calculator. The ability for the user to input data 
must still be added.
Created on Thu Oct 27 20:13:15 2016

@author: ThinkPad
"""

def hotel_cost(nights):
    return 140 * nights
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
def rental_car_cost(days):
    rental_fee = 40 * days
    if days >= 7:
        rental_fee -= 50
    elif days >= 3 and days < 7:
        rental_fee -= 20
    return rental_fee
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
print trip_cost("Los Angeles", 5, 600)