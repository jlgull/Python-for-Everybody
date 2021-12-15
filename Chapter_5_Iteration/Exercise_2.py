#!/bin/python3
#
# Author: Jonathan Heard
# Based on work from the book "Python for Everybody"
#
#
# Chapter 5 Exercise 2 on Page 65
#

# Program to accept numbers until "done" is entered.
#   When "done" is entered return: Maximum and Minimum
#   If a none number is entered, use try & except to give an error
#   message and then request another number.
#
# Set initial values for maximum & minimum

maximum = minimum = None

# Use try to catch non-numeric data entry

# try:

while True:
    # Use input() to gather a list of numbers
    #
    rawData = input("Enter an integer, to quit enter 'done': ")
    if rawData == "done":
        break
    try:
        waste = int(rawData)
        if maximum is None or rawData > maximum:
            maximum = rawData
        if minimum is None or rawData < minimum:
            minimum = rawData
    except:
        print("\n\tPlease enter only numbers!")

# When "done" is entered, print the Maximum and Minimum values entered

# Print the results
print("\nThe Maximum value entered was:", maximum)
print("The Minimum value entered was:", minimum)

