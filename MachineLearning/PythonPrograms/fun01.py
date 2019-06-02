# demo of functions

def functioncall1() :
	print " the call of the functioncall1 is executed"
	functioncall2()
	print " end of function1"
	
def functioncall2() :
	print "the call of the functioncall2 is executed"
	print "end of function2"
	
print "Executing first line in Main"
functioncall1()
print "Back to main body"
