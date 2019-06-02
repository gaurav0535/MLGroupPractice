class wipro:
    def __init__(self):
	    print " Constructor is executed", self
	
	def display(self):
	    print "Display methord is executed", self
		
	def __del__(self) :
	    print "Destructor executed", self
	
m = wipro()
n = wipro()

m.display()
n.display()

print " Thank you"