#demo of functions FUN009.py
def functioncall(* args):
	print " the type of X is " ,type(args)
	print " the values passed in one go is " , args
	for x in args
		print x
	print "End of function"
	
print "executing first line in body"
functioncall(1)
functioncall('a')
functioncall(1,2,3,4,5)
functioncall(1,'a',2,'b',3,'c',4,'d',5,'e')
print " Back to main body"