#!/usr/bin/env python3
# # Python for Everybody, Chapter 14 - Object Oriented Programming, Example 4

from party import PartyAnimal

class CricketFan(PartyAnimal):
    points = 0
    def six(self):
        self.points += 6
        self.party()
        print(self.name,"points",self.points)

s = PartyAnimal("Sally")
s.party()
j = CricketFan("Jim")
j.party()
j.six()
print(dir(j))

