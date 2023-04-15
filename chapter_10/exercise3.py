# Python for Everybody, Chapter 10 - Tuples, Exercise 3

# Write a program that reads a file and prints the letters in
# decreasing order of frequency. Your program should convert all
# the input to lower case and only count the letters a-z. Your
# program should not count spaces, digits, punctuation, or anything
# other than the letters a-z. Find text samples from several
# different languages and see how letter frequency varies between
# languages.

letterCount = {}

fname = input("Please enter a file name to evaluate: ")

try:
    fhand = open(fname)
except:
    print("The file name you entered was invalid: " + fname)
    exit()

for line in fhand:
    words = line.split()
    for word in words:
        if word.isalpha():
            characters = list(word)
            for char in characters:
                if char.isalpha():
                    letterCount[char.lower()] = letterCount.get(char.lower(), 0) + 1

sortedList = []
for key, value in letterCount.items():
    sortedList.append((value, key))

sortedList.sort(reverse = True)

for item in sortedList:
    print(item[1] + " " + str(item[0]))

