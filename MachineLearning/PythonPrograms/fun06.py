# demo of function

def functioncall():
	print " the address indite function is " ,id(x),id(y)
	print " the call of the functioncall is executed"
	print " the values accessed in function %d and %d " % (x,y)
	
	
x=10; y=20
print "Executing first line in Body"

print " the address inside main function is " , id(x),id(y)
functioncall()
print " back to main body"
print " the values after function call is %d  and %d" % (x,y)
	