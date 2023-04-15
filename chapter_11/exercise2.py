# Python for Everybody, Chapter 11 - Regular Expressions, Exercise 2

# Write a program to look for lines of the form:
#
# New Revision: 39772
# Extract the number from each of the lines using a regular
# expression and the findall() method. Compute the average of the
# numbers and print out the average as an integer.

import re

fhand = open('mbox.txt')

count = 0
total = 0

for line in fhand:
    line = line.rstrip()
    if re.findall('rev=([0-9]+)', line):
        count += 1
        x = re.findall('rev=([0-9]+)', line)
        total += int(x[0])

average = total / count
print("There were a total of " + str(count) + " revision occurences.")
print("The average of the revision total is: " + str(average))
