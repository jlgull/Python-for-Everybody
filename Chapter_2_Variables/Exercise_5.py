#!/bin/python3
#
# Author: Jonathan Heard
# Based on work from the book "Python for Everybody"
#
# Chapter 2 Exercises, on Page 20
#
# Exercise 5
#
# Request a temperature in Degrees Celsius and print
#   the results in Degrees Fahrenheit

degreesC = float(input("\nEnter a temperature in Degrees Celsius: "))

print(degreesC, "Degrees Celsius =", ((degreesC / 5) * 9) + 32, "Degrees Fahrenheit")
