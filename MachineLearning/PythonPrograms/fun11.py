#demo

res=lambda x,y:x+y

print "executing the main funtions"
a=10
b=20
z=res(a,b)

print "The sum of two numbers %d, %d is %d" %(a,b,z)
a=1.2
b=2.3
z=res(a,b)
print " the sum of two numbers %f, %f is %f" %(a,b,z)

a='m'
b='n'
z=res(a,b)
print " the sum of two numbers %s, %s is %s" %(a,b,z),type(res)