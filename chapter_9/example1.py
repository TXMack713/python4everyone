# Python for Everybody, Chapter 9 - Dictionaries, Example 1

# We will write a Python program to read through the lines of the
# file, break each line into a list of words, and then loop through
# each of the words in the line and count each word using a
# dictionary. The example file is romeo.txt

counts = {}
fhand = open('romeo.txt')

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1


print(counts)