# Python for Everybody Chapter 7 - Files, Exercise 1

# Write a program to read through a file
# and print the contents of the file (line by line)
# all in upper case.

fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("The file name you entered cannot be opened: ", fname)
    exit()

for line in fhand:
    print(line.upper())

fhand.close()
