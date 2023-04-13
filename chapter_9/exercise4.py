# Python for Everybody, Chapter 9 - Dictionaries, Exercise 4

# Add code to the program from exercise 3 to figure out who has the
# most messages in the file. After all the data has been read and
# the dictionary has been created, look through the dictionary using
# a maximum loop (see Chapter 5: Maximum and minimum loops) to find
# who has the most messages and print how many messages the person
# has.

count = {}

fhand = open("mbox.txt")

for line in fhand:
    if line.startswith("From "):
        words = line.split()
        if len(words) == 0 or len(words) < 3: continue
        count[words[1]] = count.get(words[1], 0) + 1

# placeholder for future code
print(count)