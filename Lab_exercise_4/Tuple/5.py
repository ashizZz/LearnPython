# create a tuple
t1 = (4, 6, 2, 8, 3, 1)
print(t1)
t1 = t1 + (9,)
print(t1)
# adding items in a specific index
t1 = t1[:5] + (15, 20, 25) + t1[:5]
print(t1)

