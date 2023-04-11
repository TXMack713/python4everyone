# Python for Everybody, Chapter 8 - Lists, Exercise 1

# Write a function called chop that takes a list and modifies it,
# removing the first and last elements, and returns None. Then
# write a function called middle that takes a list and returns a
# new list that contains all but the first and last elements.


# myList = inp("Please enter a list of entries: ")
def chop():
    myList = []
    entry = input("Please enter a list of entries, press enter after each entry. Press 'end' when you are done: ")
    while True:
        if entry.lower() == "end":
            break
        else:
            myList.append(entry)
            entry = input()

    orig = myList[:]
    del myList[0]
    del myList[len(myList) - 1]
    print("Here's the original list:")
    print(orig)
    print("Here's the updated list:")
    print(myList)

chop()