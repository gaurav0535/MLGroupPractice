import sys
res=0
for x in sys.argv[1:]:
    res +=eval(x)
print "sum of all values given in command line is ", res