#!/bin/python3
#
# Author: Jonathan Heard
# Based on work from the book "Python for Everybody"
#

# Basic countdown loop
n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blastoff!\n")

# Infinite Loop with break

while True:
    line = input("> ")
    if line == 'done':
        break
    print(line)
print("Done!\n")

# Infinite Loop using continue

while True:
    line = input("> ")
    if line[0] == "#":
        continue
    if line == 'done':
        break
    print(line)
print("Done!\n")

# Using a for loop to read a list

friends = ["Samson","Jason","Michael"]
for friend in friends:
    print("Happy New Year:", friend)
print("Done\n")


# Using a loop to count the number of  items in a list

count = 0
for iterval in [3, 4, 12, 9, 74, 15]:
    count = count + 1
print("\nNumber of items in list:", count)

# Using a loop to sum the items in a list

count = 0
for iterval in [3, 4, 12, 9, 74, 15]:
    count = count + iterval
print("\nThe sume of the items in list is:", count)

# Using a loop to find the largest item in list

largest = None
print("\nBefore:", largest)
for iterval in [3, 4, 12, 9, 74, 15]:
    if largest is None or iterval > largest:
        largest = iterval
    print("Loop:", iterval, largest)
print("\nLargest Number in list is:", largest)

# Using a loop to find the smallest item in list

smallest = None
print("\nBefore:", smallest)
for iterval in [3, 4, 12, 9, 74, 15]:
    if smallest is None or iterval < smallest:
        smallest = iterval
    print("Loop:", iterval, smallest)
print("\nSmallest Number in list is:", smallest)

