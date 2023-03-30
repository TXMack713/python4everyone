# Python for Everybody chapter 5 - Iterations, exercise 1

entry = ''
total = 0
count = 0
while entry != 'done' or entry != 'Done' or entry != 'DONE':
    try:
        entry = input("Enter a number: ")
        if entry == 'done' or entry == 'Done' or entry == 'DONE':
            break;
        total += float(entry)
        count += 1
    except:
        print("Invalid entry!")

average = total / count
print("The total is " + str(total))
print("The total number of numeric entries is: " + str(count))
print("The average of the entries is: " +  str(average))