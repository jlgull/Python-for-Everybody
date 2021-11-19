#!/bin/python3
#
# Author: Jonathan Heard
# Based on work from the book "Python for Everybody"
#
#
# Chapter 3 Exercises on Page 40
#
# Exercise 1, revise pay calculation to
#   account for Time and a half for hours worked
#   over 40 hours.
#
# Use Input() to gather hours and rate of pay,
#   then compute gross pay

hours = input("Enter Total Hours worked: ")

rate = input("Enter Rate of pay: ")

# Calculate pay owed

if int(hours) <= 40:
    totalPay = float(hours) * float(rate)
else:
    totalPay = (40 * float(rate)) + ((float(hours) - 40) * (float(rate) * 1.5))

# print out total pay due

print("Your Pay is $", totalPay)
