# Python for Everybody, Chapter 13 - Using Web Services, Example 3

# Working with XML (extensible markup language)

import xml.etree.ElementTree as ET
input = '''
    <stuff>
        <users>
            <user x="2">
                <id>001</id>
                <name>Chuck</name>
            </user>
            <user x="7">
                <id>009</id>
                <name>Brent</name>
            </user>
        </users>
    </stuff>'''

stuff = ET.fromstring(input)

lst = stuff.findall("users/user")
print("Original user count: " + str(len(lst)))

lst2 = stuff.findall("user")
print("New user count: " + str(len(lst2)))
