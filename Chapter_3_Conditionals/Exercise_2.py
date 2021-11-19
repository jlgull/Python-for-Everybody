#!/bin/python3
#
# Author: Jonathan Heard
# Based on work from the book "Python for Everybody"
#
#
# Chapter 3 Exercises on Page 40
#
# Exercise 2, revise pay calculation to use try and except
#   to handle non-numeric entries gracefully.
#   The program will accept hours greater than 40
#   and then account for pay rate being 1.5 * rate
#   half for hours worked over 40 hours.
#
# Use try to catch non-numeric data entry

try:

    # Use Input() to gather hours and rate of pay,
    #   then compute gross pay

    hours = float(input("Enter Total Hours worked: "))

    rate = float(input("Enter Rate of pay: "))

    # Calculate pay owed

    if int(hours) <= 40:
        totalPay = float(hours) * float(rate)
    else:
        totalPay = (40 * float(rate)) + ((float(hours) - 40) * (float(rate) * 1.5))

    # print out total pay due

    print("Your Pay is $", totalPay)

#
# If non-numeric data is entered, print the following message
except:
    print("\n\tPlease enter only numbers!")
