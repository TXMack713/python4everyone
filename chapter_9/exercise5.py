# Python for Everybody, Chapter 9 - Dictionaries, Exercise 5

# This program records the domain name (instead of the address)
# where the message was sent from instead of who the mail came from
# (i.e., the whole email address). At the end of the program, print
# out the contents of your dictionary.

count = dict()

fhand = open("mbox.txt")

for line in fhand:
    if line.startswith("From "):
        words = line.split()
        if len(words) == 0 or len(words) < 3: continue
        sender = words[1].split("@")
        count[sender[1]] = count.get(sender[1], 0) + 1


print(count)
