from math import *
print('Решение квадратноро уровнения вида: ax^2+bx+c=0')

a = int(input ('Введите значение a: '))
print (str(a) + "x^2+bx+c=0" )

b = int(input ('Введите значение b: '))
if b>=0:
	print (str(a) + "x^2+%sx+c=0" % (b) )
else: print (str(a) + "x^2%sx+c=0" % (b) )

c = int(input ('Введите значение c: '))
if (b>=0) and (c>=0):
	print (str(a) + "x^2+%sx+%s=0" % (b,c) )
elif (b<=0) and (c>=0):
	print (str(a) + "x^2%sx+%s=0" % (b,c) )
elif (b>=0) and (c<=0):
	print (str(a) + "x^2+%sx%s=0" % (b,c) )

else: print (str(a) + "x^2%sx%s=0" % (b,c) )

d = int((b*b)-4*a*c)
if d>0:
	print ('Дискриминант равен: ' + str(d) )

	x1 = int( ( -b+sqrt(d) ) / (2*a) )
	print('x1 равен: ' + str(x1))

	x2 = int( ( -b-sqrt(d) ) / (2*a) )
	print('x2 равен: ' + str(x2))

elif d==0:
	x = int( -b/(2*a) )
	print ('Дискриминант равен: ' + str(d) )
	print('X равен: ' + str(x))
else:
	print ('Дискриминант равен: ' + str(d) )
	print('Корней нет')
