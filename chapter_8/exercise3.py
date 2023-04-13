# Python for Everybody, Chapter 8 - Lists, Exercise 3

# Rewrite the guardian code from the example in exercise 2 without
# the two if statements. Instead, use a compound logical expression
# using the or logical operator with a single if statement.

fhand = open("mbox.txt")

for line in fhand:
    words = line.split()
    if len(words) == 0 or not line.startswith("From") or len(words) < 3: continue
    print(words[2])
