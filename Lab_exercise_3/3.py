def showNumbers (Limit):
    for i in range(Limit+1):
        print(i)
     if i%2==0:
         return 'Even'
     else:
         return 'false'

x = int(input('Enter any number: '))
a =showNumbers(x)
print('The given limit num is',a)