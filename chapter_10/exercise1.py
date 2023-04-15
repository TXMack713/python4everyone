# Python for Everybody, Chapter 10 - Tuples, Exercise 1

# Revise a previous program as follows: Read and parse the “From”
# lines and pull out the addresses from the line. Count the number
# of messages from each person using a dictionary.
#
# After all the data has been read, print the person with the most
# commits by creating a list of (count, email) tuples from the
# dictionary. Then sort the list in reverse order and print out the
# person who has the most commits.

count = {}

fhand = open("mbox.txt")

for line in fhand:
    if line.startswith("From "):
        words = line.split()
        if len(words) == 0 or len(words) < 3: continue
        count[words[1]] = count.get(words[1], 0) + 1

sortedList = []
for key, value in count.items():
    sortedList.append((value, key))

sortedList.sort(reverse = True)

print(sortedList[0][1] + " " + str(sortedList[0][0]))
