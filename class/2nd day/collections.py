# bility to multiple items in a variable

from typing import Tuple

"""
List - []
Tuple
set
Dictionary


a = [1, 2, 3, 4, 5]  # List

b = (1, 2, 3, 4, 5)  # Tuple

c = {1, 2, 3, 4, 5}  # Set

"""
"""
# List

a = [1, 2, "strings", 10.5]
print(a, type(a))

#ordered(indexes)
print(a[3])

#changeable
a[2] = "hello"
print(a)

#allows duplicates
a.append(1)
print(a)

#Tuple , sensitive information not to be changeable
a = (1, 2, "strings", 10.5)
print(a, type(a))

#ordered(indexes)
print(a[3])

#not changeable
#a[2] = "hello"
#print(a)

#allows duplicates
a.append(1)
print(a)
"""
#Set
#a = {'a', 'b', a , b} # no duplicates allowed / unordered / 
#print(a, type(a))

a = {'a', 'b'}
b = {'a', 'c', 'b'}
z = a.intersection(b)

"""
Task:
lsit,str,tuple,set - work out
dictionary



"""