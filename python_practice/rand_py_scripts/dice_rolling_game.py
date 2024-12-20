# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 21:03:29 2016

@author: ThinkPad
"""

"""This program rolls a pair of dice and askes the user to input a number. Based on the number input by the user the program will determine a winner."""
#import necessary modules
from random import randomint
from time import sleep

def get_user_guess(): #define function to prompt user guess
  user_guess = int(raw_input("Guess a number: "))
  return user_guess

def roll_dice(number_of_sides): #define possible value combinations
  first_roll = randomint(1, number_of_sides)
  second_roll = randomint(1, number_of_sides)
  max_val = number_of_sides * 2
  #provide user with max value possible
  print "Maximum possible value rolled is: " + str(max_val)
  sleep(1) #simulate thinking
  user_guess = get_user_guess()
  if user_guess > max_val: #pervent user from entering invalid guess
    print "No guessing higher than the maximum possible value!"
    return
    else:
      print "Rolling..."
      sleep(2) #simulate rolling dice
      print "The first value is: %d" %first_roll
      sleep(1)
      print "Rolling again..."
      sleep(2)
      print "The second value is: %d" %second_roll
      sleep(1)
      total_roll = first_roll + second_roll
      print total_roll
      print "Result..."
      sleep(1)
      if user_guess > total_roll:
        print "Congratulations, you've won!"
        return
      else:
        print "Sorry, you've lost."
        return
roll_dice(6)