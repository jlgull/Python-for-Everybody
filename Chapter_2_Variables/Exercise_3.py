#!/bin/python3
#
# Author: Jonathan Heard
# Based on work from the book "Python for Everybody"
#
# Chapter 2 Exercises, on Page 20
#
# Exercise 3
#
# Use Input() to gather hours and rate of pay,
#   then compute gross pay

hours = input("Enter Hours: ")

rate = input("Enter Rate of pay: ")

print("Your Pay is", float(hours) * float(rate))
