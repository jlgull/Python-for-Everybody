#!/usr/bin/env python3

# Practice opening and printing file data

fhand = open("mbox-short.txt")
count = 0

for line in fhand:
    if line.startswith("From"):
        count += 1
        print(line)
print(f"Total \"From\" lines: {count}")
# End of program
