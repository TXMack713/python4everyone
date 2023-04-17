# Python for Everybody, Chapter 12 - Networked Programs, Exercise 2

# Change your socket program so that it counts the number of
# characters it has received and stops displaying any text after
# it has shown 3000 characters. The program should retrieve the
# entire document and count the total number of characters and
# display the count of the number of characters at the end of the
# document.

import socket

link = input("Enter a url to search. Please include https:// or http:// where necessary: ")

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
count = 0

try:
    domain = ''
    if link.startswith("http"):
        domain = link.split("://")
        mysock.connect((domain[1], 80))
    else:
        mysock.connect((link, 80))

    string = 'GET ' + link + ' HTTP/1.0\r\n\r\n'
    print(string)
    cmd = string.encode()
    mysock.send(cmd)

except:
    print("The url you entered is invalid.")
    exit()

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    count += len(data)
    if(count >= 3000):
        continue
    else:
        print(data.decode(), end="")

print("\n\nThe total data amount received by the browser is: " + str(count))

mysock.close()
