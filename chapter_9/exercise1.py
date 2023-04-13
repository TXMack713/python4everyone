# Python for Everybody, Chapter 9 - Dictionaries, Exercise 1

# Write a program that reads the words in words.txt and stores them
# as keys in a dictionary. It doesn’t matter what the values are.
# Then you can use the in operator as a fast way to check whether a
# string is in the dictionary.

word_dict = {}
fhand = open("words.txt")
for line in fhand:
    words = line.split()
    for word in words:
        word_dict[word] = ""


print(word_dict)