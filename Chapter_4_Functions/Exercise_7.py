#!/bin/python3
#
# Author: Jonathan Heard
# Based on work from the book "Python for Everybody"
#
#
# Chapter 4 Exercises on Page 54
#

# Exercise 7, Revise the program from previous chapter
#   to request a score between 0.0 and 1.0.
#   If score is out of range or non-numeric
#   print an error message. If the score is between 0.0 and 1.0
#   return the appropriate grade, using the function computegrade
#
#   Define the function, computegrade


def computegrade(score):
    if score > 1.0:
        return("INVALID SCORE ENTERED!")
    elif score >= 0.9:
        return("A")
    elif score >= 0.8:
        return("B")
    elif score >= 0.7:
        return("C")
    elif score >= 0.6:
        return("D")
    else:
        return("F")


# Use try to catch non-numeric data entry

try:
    # Use Input() to gather grade.

    score = float(input("Enter a score between 0.0 and 1.0: "))

    # Print the results of the function
    print("Your grade is \b", computegrade(score))


#
# If non-numeric data is entered, print the following message
except:
    print("\n\tNumeric Data Required!")
