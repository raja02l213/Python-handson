#    0  1     2    3     4      5       6       7   8    9   10  # Positive Index
a = [1,2.33,"hi",True,'alpha','beta','theta',33.44,666,100,12.33]
#                                                   -3  -2   -1  
print(a)            # prints whole List
print(a[7])         # access the positive Index
print(a[-2])        # access the negative Index
print(a[1:9])       # start index : end before index;   
print(a[3:-1])      # start index : end before index;   
print(a[4:])        # start index : till end of List;       
print(a[:9])        # from start of List: end before index
print(a[:])         # from start of List: till end of List
print(a[0:11:2])    # start index : end before index : jump
print(a[::3])       # from start of List: till end of List: jump
print(a[::-1])      # reversing a List using jump as -1
