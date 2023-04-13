# Python for Everybody, Chapter 9 - Dictionaries, Example 2

# We will write a Python program to read through the lines of the
# file, break each line into a list of words, and then loop through
# each of the words in the line and count each word using a
# dictionary. The example file is romeo.txt and we are using the
# string.punctuation method to help strip all punctuation from the
# file.

import string


fname = input("Please enter a file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened: " + fname)
    exit()

counts = {}

for line in fhand:
    line.rstrip()
    line.translate(line.maketrans("", "", string.punctuation))
    line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts.items())
