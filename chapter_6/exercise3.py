# Python for Everybody - chapter 6, exercise 3
# Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.

# Original code:
# word = 'banana'
# count = 0
# for letter in word:
#   if letter == 'a':
#       count = count + 1
# print(count)

def count(string, letter):
    count = 0
    for char in string:
        if char.lower() == letter:
            count += 1

    print("Here's the starting string: " + string)
    print("Here's the letter we're looking for: " + letter)
    print("Here's the number of times the chosen letter appeared in the string: " + str(count))
    # print(count)


message = "Hello, World!"
count(message, "l")

greeting = "Howdy, Y'all!"
count(greeting, "y")

farewell = "Now y'all take care now, ya here?!"
count(farewell, "e")