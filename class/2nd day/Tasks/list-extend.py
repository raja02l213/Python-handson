"""
a = [1,22,3.43,1,81,17,14,1,21]
b = [111,222,333]
a.extend(b) 
print(a)
print(b)
"""

a = [1,22,3.43,1,81,17,14,1,21]
b = (111,222,333)   # Its a tuple
a.extend(b) 
print(a)
print(b)
