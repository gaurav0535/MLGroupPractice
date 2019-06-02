#demo of functions

def functioncall1() :
	print "the call of the second functioncall is executed"
	print "end of function", dir()
	print 'the local members are acessible are " ' , locals()
	print 'the global members are acessible are " ' , globals()
	
	
	
a=10
b='Wipro'

print "Execiting first line in boday"
functioncall1()
print "Function is " , functioncall1
print "back to main body"
print 'the namespace contents are ' , dir()