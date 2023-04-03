# Python for Everybody - chapter 6, exercise 2
# Given that message is a string, what does message[:] mean?

message = "Hello, Wolrd"

print("Here's the original string: " + message)

print("string[:index] means slice from the beginning of the string to one position before the ending index")
print(message[:5])

print("string[index:] means slice starting at the given starting index through to the end of the string")
print(message[7:])

print("string[:] messages slice the entire string")
print(message[:])
