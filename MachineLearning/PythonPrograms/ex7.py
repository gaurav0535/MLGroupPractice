# Exceptions in python

try :
	X = input("Enter the first number")
	Y = input("Enter the second number")
	print " The values stored are", X,Y
	res = X/Y
	print " the result of two divided numbers by Zero", res
except ZeroDivisionError:
	print " trying to divide by zero"
except TypeError:
	print "Given non compatable values to divide"
except NameError:
	print "Error with the given values to program"
except Exception:
	print "This is the default exception handler"
else:
	print "else block is executed only if there is no error"
finally :
	print "Finally will get executed all times"
	