class wipro:
    def __init__(self,x,y):
	    self.a=x;
	    self.b=y;
			print " Constructor is executed"
	def display(self):
	    print "display method is executed",self,self.a,self.b
	
	def __del__(self) :
	    print "destructor executed", self
		
m = wipro(1,2)
n = wipro(3,4)

m.display()
n.display()

print "Object attributed of M is ", m.a,m.b
print "Object attributed of N is ", n.a,n.b

print ' the components of class is ', dir(wipro)
print ' the components of class is ', dir(m)
del m

print 'Destructor manually executed'
print ' the default container component', dir()



	