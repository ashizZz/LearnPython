from copy import deepcopy

# create a tuple
a = ("HELLO", 'world', [], 2)
print(a)
# make a copy of a tuple using deepcopy() function
a_colon = deepcopy(a)
a[2].append('softwarica')
print(a_colon)
print(a)
