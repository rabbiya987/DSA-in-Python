#Hashset 

s=set()
print(s)

#Adding items - O(1)
s.add(1)
s.add(2)
s.add(3)
print(s)

#Searching for an element - O(1)
if 2 in s:
    print(True)

#Removing an element - O(1)
s.remove(3)
print(s)

#Suppose we got a string having duplicates
string="aaaaaaaaaaabbbbbbbbbb" #searching in atring is O(n)
sett=set(string) #O(n) where n is the length of string
print(sett)  #will contain only unique elements of string

#Extras
from collections import Counter
print(Counter(string))