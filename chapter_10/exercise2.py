# Python for Everybody, Chapter 10 - Tuples, Exercise 2

# This program counts the distribution of the hour of the day for
# each of the messages. You can pull the hour from the “From” line
# by finding the time string and then splitting that string into
# parts using the colon character. Once you have accumulated the
# counts for each hour, print out the counts, one per line, sorted
# by hour as shown below.

count = dict()

fhand = open("mbox.txt")

for line in fhand:
    if line.startswith("From "):
        words = line.split()
        if len(words) == 0 or len(words) < 3: continue
        timestamp = words[5].split(":")
        count[timestamp[0]] = count.get(timestamp[0], 0) + 1

sortedList = []

for key, value in count.items():
    sortedList.append((value, key))

sortedList.sort(reverse = True)

for item in sortedList:
    print(item[1] + " " + str(item[0]))

