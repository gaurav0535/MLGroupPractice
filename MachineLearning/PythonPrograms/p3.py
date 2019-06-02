import sys,math
if(len(sys.argv) !=2):
	print "Error: Syntax command <int argument>"
	print "please provide 1 argument"
	sys.exit(1)
print "the length of the command line arguments is : ", len(sys.argv)
print " the given values at command line is: ", sys.argv
print " the first value in command line arguments is :" , sys.argv[0]
print " the first value in command line arguments is :" , sys.argv[1]

res = math.sqrt(float(sys.argv[1]))
print " square root of the given number is :", res
