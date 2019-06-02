#demo functions

def functioncall(a,b) :
	print "the call of the functioncall is executed"
	print "te address of a and b in function " , id(a),id(b)
	print "the values passed to function %d and %d in function " % (a,b)
	print "end of function"
	
	
	
print "Executing first line in body";
x=10
y=20

print "the address of x and y is", id(x),id(y)
functioncall(x,y)
print "back to main"
	