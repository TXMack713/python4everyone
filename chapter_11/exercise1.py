# Python for Everybody, Chapter 11 - Regular Expressions, Exercise 1

# Write a simple program to simulate the operation of the grep
# command on Unix. Ask the user to enter a regular expression and
# count the number of lines that matched the regular expression:


expression = input("Please enter a regular expression for file searching: ")

print(type(expression))

count = 0

fhand = open('mbox.txt')

import re

for line in fhand:
    line = line.rstrip()
    if re.findall(expression, line):
        count += 1

print("There were " + str(count) + " lines that matched " + expression)
