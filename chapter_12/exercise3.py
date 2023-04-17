# Python for Everybody, Chapter 12 - Networked Programs, Exercise 3

# Use urllib to replicate the previous exercise of (1) retrieving
# the document from a URL, (2) displaying up to 3000 characters,
# and (3) counting the overall number of characters in the
# document. Don’t worry about the headers for this exercise, simply
# show the first 3000 characters of the document contents.

import urllib.request

link = input("Enter a url to search. Please include https:// or http:// where necessary: ")

count = 0

fhand = urllib.request.urlopen(link)

for line in fhand:
    words = line.decode().split()
    for word in words:
        count += len(list(word))

    if count <= 3000:
        print(line.decode())


print("\n\nThe total number of characters retrieved from the webpage is: " + str(count))
