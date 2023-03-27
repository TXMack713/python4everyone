try:
    hours = float(input("Please enter the number of hours worked "))
except:
    print("Please enter the number of hours worked in the form of a number.")

try:
    rate = float(input("Please enter the rate of pay "))
except:
    print("Please enter the pay rate in the form of a number.")

if hours <= 40:
    pay = hours * rate
elif hours > 40:
    overtimeHours = hours - 40
    baseHours = 40
    overtimeRate = rate * 1.5
    pay = (baseHours * rate) + (overtimeHours * overtimeRate)

print("The total pay due is: " + str(pay))
