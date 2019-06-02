#demo of funvtions

def functioncall1():
	x=100;y=200
	print " the address inside function is " , id(x),id(y)
	print " the call of the functioncall is execited"
	print " the valies inside the funtion %d and %d " % (x,y)
	print 'Locals: ', locals()
	print 'globals: ', globals()
	
x=10;y=20

print " executing first line in body"
print " the address inside main function is " , id(x),id(y)
functioncall1()
print " back to main body"
print " the values after function call is %d and %d" % (x,y)