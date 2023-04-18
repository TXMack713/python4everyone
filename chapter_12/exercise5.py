# Python for Everybody, Chapter 12 - Networked Programs, Exercise

# (Advanced) Change the socket program so that it only shows data
# after the headers and a blank line have been received. Remember
# that recv receives characters (newlines and all), not lines.

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
        output = data.decode()
        print("There are a total of " + str(len(output))+ " characters")
        location = output.index('<')
        print(output[location:], end="")


print("\n\nThe total data amount received by the browser is: " + str(count))

mysock.close()
