from math import ceil
# Read an integer:
a = int(input("Gr. a: "))
b = int(input("Gr. b: "))
c = int(input("Gr. c: "))
# Math

classa=ceil(a/2)
classb=ceil(b/2)
classc=ceil(c/2)
classall=(classa+classb+classc)

print("%s" % classall)