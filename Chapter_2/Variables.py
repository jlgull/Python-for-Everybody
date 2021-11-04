#!/bin/python3
#
# Author: Jonathan Heard
# Based on work from the book "Python for Everybody"
#
# Exercises 2.15
# Exercise 2
#
# Use Input() to gather names and print them

name = input("Enter your first name: ")

print("Hello", name)

# Exercise 3
#
# Use Input() to gather hours and rate of pay,
#   then compute gross pay

hours = input("Enter Hours: ")

rate = input("Enter Rate of pay: ")

print("Your Pay is", float(hours) * float(rate))

# Exercise 4
#
# Use type to determine the data type for each output

width = 17
height = 12.0

print("\nwidth =", width)
print("height =", height)

print("\nwidth // 2 =", (width // 2), type(width//2))

print("\nwidth / 2.0 =", (width / 2.0), type(width/2.0))

print("\nheight / 3 =", (height / 3), type(height/3))

print("\n1 + 2 * 5 =", (1 + 2 * 5), type(1 + 2 * 5))

# Exercise 5
#
# Request a temperature in Degrees Celsius and print
#   the results in Degrees Fahrenheit

degreesC = float(input("\nEnter a temperature in Degrees Celsius: "))

print(degreesC, "Degrees Celsius =", ((degreesC / 5) * 9) + 32, "Degrees Fahrenheit")
