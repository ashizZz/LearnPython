def getSum(a):
    s1 = 0
    while (a != 0):
        s1 = s1 + int(a % 10)
        a = int(a/10)

    return s1


n = 687
print(getSum(n))