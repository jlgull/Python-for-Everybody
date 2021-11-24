#!/bin/python3
#
# Author: Jonathan Heard
# Based on work from the book "Python for Everybody"
#
#
# Chapter 4 Exercise 2 & 3 on Page 49
#

""" For exercise 2, the call to the fucntion was placed
    before the actual functions, it was at line 10 as noted in the error message.
    Here is the error message received.

Traceback (most recent call last):
  File "/home/jlh/Python_projects/Python-for-Everybody/Chapter_4_Functions/Exercise_2&3.py", line 10, in <module>
    repeat_lyrics()
NameError: name 'repeat_lyrics' is not defined"""

""" For exercise 2, the function call was placed here.
    After receiving the error information, the call was commented out.
    repeat_lyrics()"""

# Create several Functions

"""For exercise 3, the repeat_lyrics function was placed before
        the print_lyrics function to see what happens.
        The results were that the program executed correctly."""

def repeat_lyrics():
    print_lyrics()
    print_lyrics()


def print_lyrics():
    print("\nI'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")


print(print_lyrics)

print(type(print_lyrics))

print_lyrics()

# After exercise 2, moved the function call back to the end
#   of the program.

repeat_lyrics()
