# Python for Everybody - chapter 6, exercise 1
# Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.

message = "Hello, World!"

length = len(message)
index = length - 1

print("I started with: " + message)
print("Then I printed: ")

while index >= 0:
    print(message[index])
    index -= 1

