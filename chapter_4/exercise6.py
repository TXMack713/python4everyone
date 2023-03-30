# Python for Everybody chapter 4 - Functions, exercise 6
# Creating a compute pay function to calculate pay for regular and overtime pay

try:
    hours = float(input("Please enter the total number of hours worked: "))
except:
    hours = float(input("Please enter a valid number for the hours worked: "))

try:
    rate = float(input("Please enter the pay rate: "))
except:
    rate = float(input("Please enter a valid number for the pay rate: "))

def computePay(hours, rate):
    if hours > 40:
        overtimeHours = hours - 40
        pay = (40 * rate) + (overtimeHours * 1.5 * rate)
        return pay
    else:
        pay = hours * rate
        return pay


salary = computePay(hours, rate)

print("Total pay: " + str(salary))