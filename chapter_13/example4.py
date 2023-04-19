# Python for Everybody, Chapter 13 - Using Web Services, Example 4

# Working with JSON (JavaScript Object Notation)

# JSON example
# {
#     "name" : "Chuck",
#     "phone" : {
#         "type" : "intl",
#         "number" : "+1 734 303 4456"
#     },
#     "email" : {
#         "hide" : "yes"
#     }
# }

import json

data = '''
    [
        { 
            "id" : "001",
            "x" : "2",
            "name" : "Chuck"
        },
        {
            "id" : "009",
            "x" : "7",
            "name" : "Brent"
        }
    ]'''

info = json.loads(data)
print("User count: " + str(len(info)))

for item in info:
    print("Name", item["name"])
    print("Id", item["id"])
    print("Attribute", item["x"])

