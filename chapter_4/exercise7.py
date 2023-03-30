# Python for Everybody chapter 4 - Functions, exercise 7

def computeGrade(grade):
    if grade >= 0.9:
        print("A")
    elif grade >= 0.8:
        print("B")
    elif grade >= 0.7:
        print("C")
    elif grade >= 0.6:
        print("D")
    elif grade < 0.6:
        print("F")


try:
    score = float(input("Please enter a score between 0.0 and 1.0: "))
    if (score < 0) or (score > 1):
        print("Error, the number you entered is outside of the range")
        score = float(input("Please enter a score between 0.0 and 1.0: "))
    computeGrade(score)
except:
    score = float(input("Please enter a score between 0.0 and 1.0: "))
    if (score < 0) or (score > 1):
        print("Error, the number you entered is outside of the range")
        score = float(input("Please enter a score between 0.0 and 1.0: "))
    computeGrade(score)

