# Python for Everybody, Chapter 12 - Networked Programs, Exercise 1

# Change the socket program socket1.py to prompt the user for the
# URL, so it can read any web page. You can use split('/') to break
# the URL into its component parts, so you can extract the host name
# for the socket connect call. Add error checking using try and
# except to handle the condition where the user enters an
# improperly formatted or non-existent URL.

import socket

link = input("Enter a url to search. Please include https:// or http:// where necessary: ")

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
    print(data.decode(), end="")

mysock.close()
