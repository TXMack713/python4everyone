# Python for Everybody chapter 5 - Iterations, exercise 2
# Write a program that prompts the user for a list of numbers and prints out the max and min once all numbers have been entered

numberList = []
entry = None

def getNumbers():
    global entry
    print("Please enter a list of numbers pressing enter after each number. Enter an done when you are finished: ")
    while entry != "done" or entry != "Done" or entry != "DONE":
        try:
            entry = input("Number: ")
            if entry == "done" or entry == "Done" or entry == "DONE":
                break
            else:
                value = float(entry)
                numberList.append(value)
        except:
            print("Invalid entry. Please enter a number")
            continue


getNumbers()
minimum = None
maximum = None
for value in numberList:
    if minimum is None:
        minimum = value
    elif minimum >= value:
        minimum = value

    if maximum is None:
        maximum = value
    elif maximum <= value:
        maximum = value

print("The maximum number you entered is: " + str(maximum))
print("The minimum number you entered is: " + str(minimum))
print("Here's the full list of numbers you entered: " + str(numberList))

# for item in numberList:
#   print(item)
