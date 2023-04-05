# Python for Everybody Chapter 7 - Files, Exercise 2

# Write a program to prompt for a file name, and then
# read through the file and look for lines of the form
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:”
# pull apart the line to extract the floating-point number on the
# line. Count these lines and then compute the total of the spam
# confidence values from these lines. When you reach the end of the
# file, print out the average spam confidence.

fname = input("Enter a file name: ")

lineCount = 0
total = 0

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