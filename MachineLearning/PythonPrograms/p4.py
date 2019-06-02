import sys
i=1
res=0

while(i !=len(sys.argv)):
   res += int(sys.argv[i])
   i+=1
print "sum of all values", res	