class wipro :
    def display(self)
	    print " Inside display ", self

m = wipro()
n = wipro()

m.display()
n.display()

print " address of m %x and n is %x " % (id(m),id(n))
print " address of m is ", m