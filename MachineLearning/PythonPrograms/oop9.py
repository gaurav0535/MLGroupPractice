class Base:
    res=10;
	def display(self):
	    print " display of Base executed", self
	display = classmethod(display)
	
ob1 = Base();
ob1.display();

print 'Class reference :'  Base, 'Object reference:', ob1

print "Method  reference : ", ob1.display
print "Contents of Base is : ", dir(Base)
print "Contents of Object is : ", dir(ob1)
print "Dictionary contents is ", Base.__dict__