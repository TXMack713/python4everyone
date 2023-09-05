#!/usr/bin/env python3
# Python for Everybody, Chapter 14 - Object Oriented Programming, Example 2

class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

    def __del__(self):
        print("I am destructed", self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains', an)

