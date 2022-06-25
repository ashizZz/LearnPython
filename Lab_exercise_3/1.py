def compare(x,y,z):
	if x>y and x>z:
		print(f'{x} is the max among three numbers')

	if y>z and y>x:
		print(f'{y} is the max among three numbers')

	if z>x and z>y:
		print(f'{z} is the max among three numbers')

a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
c=int(input('Enter third number:'))
compare(a,b,c)