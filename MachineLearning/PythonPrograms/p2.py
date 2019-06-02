import sys

print " total params given at command line: ", len(sys.argv)
print " given values at command line: ", sys.argv
print " first params given at command line: ", sys.argv[0],type(sys.argv[0])
print " second params given at command line: ", sys.argv[1],type(sys.argv[1])
print " Thirst params given at command line: ", sys.argv[2],type(sys.argv[2])
print " Sum of params given at command line: ", int(sys.argv[1]) + int(sys.argv[2])
print " Sum of params given at command line: ", eval(sys.argv[1]) + eval(sys.argv[2])


