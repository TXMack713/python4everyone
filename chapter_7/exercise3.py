# Python for Everybody Chapter 7 - Files, Exercise 3

# Sometimes when programmers get bored or want to have a bit of
# fun, they add a harmless Easter Egg to their program. Modify the
# program that prompts the user for the file name so that it \
# prints a funny message when the user types in the exact file
# name “na na boo boo”. The program should behave normally for all
# other files which exist and don’t exist.

fname = input("Enter a file name: ")

lineCount = 0
total = 0

if fname.lower() == "na na boo boo":
    print(fname.upper() + " You have been punk'd!")
    exit()


try:
    fhand = open(fname)
    for line in fhand:
        if line.lower().startswith("x-dspam-confidence"):
            linearray = line.split(":")
            lineCount += 1
            entry = linearray[1]
            total += float(entry)
            # print(entry)

    fhand.close()
except:
    print("The file name you entered could not be opened: " + fname)
    exit()

print("The confidence sum is: " + str(total))
print("The total line count is: " + str(lineCount))
print("The average space confidence is: " + str(total / lineCount))