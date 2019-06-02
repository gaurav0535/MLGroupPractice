import sys
i=1
res=0

while(i !=len(sys.argv)):
   print "sys.argv[%d] is %s" % (i,sys.argv[i])
   if (sys.argv[i].isdigit()):
		res += int(sys.argv[i])
   i+=1
print "sum of all values", res	