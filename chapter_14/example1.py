#!/usr/bin/env python3
# Python for Everybody, Chapter 14 - Object Oriented Programming, Example 1

class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

an = PartyAnimal()
an.party()
an.party()
an.party()
PartyAnimal.party(an)

print("Type", type(an))
print("Dir ", dir(an))
print("Type", type(an.x))
print("Type", type(an.party))

