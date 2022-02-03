#!/bin/python3
#
# Author: Jonathan Heard
# Based on work from the book "Python for Everybody"
#
#
# Chapter 9 Exercise 1 on Page 120
#

"""
    Program to read the words in a file and stores
    them as keys in a dictionary.
   When "done" is entered return: Total, Count and Average
   If a none number is entered, use try & except to give an error
   message and then request another number.
"""
#
# Set initial values for Total & Count

total = count = 0

# Use try to catch non-numeric data entry

# try:

while True:
    # Use input() to gather a list of numbers
    #
    rawData = input("Enter an integer, to quit enter 'done': ")
    if rawData == "done":
        break
    try:
        total = total + int(rawData)
        count = count + 1
    except:
        print("\n\tPlease enter only numbers!")

    # When "done" is entered, calculate average
average = (total / count)

# Print the results
print("\nTotal of numbers entered is:", total)
print("Count of numbers entered:", count)
print("\tAverage of the numbers entered is:", average)

# If non-numeric data is entered, print the following message

