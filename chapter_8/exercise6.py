# Python for Everybody, Chapter 8 - Lists, Exercise 6

# Rewrite the program that prompts the user for a list of numbers
# and prints out the maximum and minimum of the numbers at the end
# when the user enters “done”. Write the program to store the
# numbers the user enters in a list and use the max() and min()
# functions to compute the maximum and minimum numbers after the
# loop completes.

entries = []
print("Please enter a list of numbers, pressing 'enter' or 'return' after each entry. Enter 'done' when finished.")

while True:
    try:
        entry = input("Enter a number: ")
        if entry.lower() == 'done':
            break
        else:
            entries.append(float(entry))
    except:
        print("Your entry was invalid. Please enter a valid number.")


print("The maximum number you entered is: " + str(max(entries)))
print("The minimum number you entered is: " + str(min(entries)))