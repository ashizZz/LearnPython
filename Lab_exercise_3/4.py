def abc(limit):
    d =0
    e= 0
    for x in range(0,limit+1,3):
        d =d+x

    for y in range(0, limit+1,5):
        e=e+y
        f =d+e
        print('The value of f is',f)
a =int(input('Enter your your number:'))
abc(a)