# using exception handler

try :
	x = input("Enter first number :")
	y = input("Enter second number :")
	
	print " the values stored are ", x,y
	
	res = x/y
	
	print " the result of 2 divided numbers are ", res
	print " i have executed:"
	
except ZeroDivisionError ,e :
	print " error encountered, try to divide number by zero"
except NameError, e:
	print " error, the given variable is not defined"
	print e
	