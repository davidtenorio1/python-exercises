""" 1. Import and test 3 of the functions from your functions exercise file.
import functions_exercises as fe
fe.cumsum()

from functions_exercises import cumsum

from functions_exercises import cumsum as cs


#How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
from itertools import permutations
combos = list(permutations('abc123', 6))
length = len(combos)
print(length)

#How many different ways can you combine two of the letters from "abcd"?
combos2 = list(permutations("abcd",2))
length2 = len(combos2)
print(length2)
"""


import json as j
with open("profiles.json") as profiles:
    data = j.load(profiles)
#Total number of users
print(len(data))

#Number of active users
is_active = []
for i in data: 
    is_active.append(i['isActive'])
string_active = str(is_active)
print(string_active.count("True"))

#Number of inactive users
is_not_active = []
for i in data: 
    is_not_active.append(i['isActive'])
string_inactive = str(is_not_active)
print(string_inactive.count("False"))

#Grand total of balances for all users












