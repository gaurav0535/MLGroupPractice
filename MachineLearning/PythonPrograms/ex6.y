# Exceptions in Python

try :
	X = input("Enter first number");
	Y = input("Enter second number");
	
	try :
		print "the values stored are", (X,Y)
		res = X/Y
		print "The result of two divided numbers are" , res
	except ZeroDivisionError,e :
		print "Internal : you are trying to divide by zero"
	except (NameError,TypeError,Exception), e:
		print "Internal : error with value given"
	