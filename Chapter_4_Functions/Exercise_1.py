#!/bin/python3
#
# Author: Jonathan Heard
# Based on work from the book "Python for Everybody"
#
#
# Chapter 4 Exercise 1 on Page 46
#

# Import Modules

import random

for i in range(10):
    x = random.random()
    if i + 1 < 10:
        print("The Loop Value of i is ", i + 1, ", the random number is:", x)
    else:
        print("The Loop Value of i is", i + 1, ", the random number is:", x)

