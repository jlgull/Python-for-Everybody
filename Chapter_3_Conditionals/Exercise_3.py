#!/bin/python3
#
# Author: Jonathan Heard
# Based on work from the book "Python for Everybody"
#
#
# Chapter 3 Exercises on Page 40
#

# Exercise 3, Create a program to request a score between
#   0.0 and 1.0. If score is out of range or non-numeric
#   print an error message. If the score is between 0.0 and 1.0
#   return the appropriate grade.
#
# Use try to catch non-numeric data entry

try:
    # Use Input() to gather grade.

    grade = float(input("Enter a grade between 0.0 and 1.0: "))

    if grade > 1.0:
        print("Bad data entered!")
    elif grade >= 0.9:
        print("A")
    elif grade >= 0.8:
        print("B")
    elif grade >= 0.7:
        print("C")
    elif grade >= 0.6:
        print("D")
    else:
        print("F")

#
# If non-numeric data is entered, print the following message
except:
    print("\n\tBad Data Entered!")
