#!/usr/bin/env python3
# # Python for Everybody, Chapter 14 - Object Oriented Programming, Example 3

class PartyAnimal:
    x = 0
    name = ''

    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)


s = PartyAnimal('Sally')
j = PartyAnimal("Jim")

s.party()
j.party()
s.party()

