#!/bin/python3
#
# Author: Jonathan Heard
# Based on work from the book "Python for Everybody"
#
#
# Chapter 4 Exercises on Page 54
#
# Exercise 6, revise pay calculation to use a function to
#   calculate the pay due, based one hours and rate.
#   and handle non-numeric entries gracefully.
#   The program will accept hours greater than 40
#   and then account for pay rate being 1.5 * rate
#   half for hours worked over 40 hours.
#
# Define a function to compute pay.
#   Accept 2 parameters and return totalPay due.


def computepay(hours, rate):
    if int(hours) <= 40:
        totalPay = float(hours) * float(rate)
    else:
        totalPay = ((40 * float(rate)) + ((float(hours) - 40) * (float(rate) * 1.5)))
    return totalPay


# End of function definition.
#
# Use try to catch non-numeric data entry

try:

    # Use Input() to gather hours and rate of pay,
    #   then compute gross pay

    hours = float(input("Enter Total Hours worked: "))

    rate = float(input("Enter Rate of pay: "))

    # Calculate pay owed

    pay = computepay(hours, rate)

    # print out total pay due

    print("Your Pay is $", pay)

#
# If non-numeric data is entered, print the following message
except:
    print("\n\tPlease enter only numbers!")
