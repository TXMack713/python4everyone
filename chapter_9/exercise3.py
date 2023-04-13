# Python for Everybody, Chapter 9 - Dictionaries, Exercise 3

# Write a program to read through a mail log, build a histogram
# using a dictionary to count how many messages have come from each
# email address, and print the dictionary.

count = {}

fhand = open("mbox.txt")

for line in fhand:
    if line.startswith("From "):
        words = line.split()
        if len(words) == 0 or len(words) < 3: continue
        count[words[1]] = count.get(words[1], 0) + 1


print(count)