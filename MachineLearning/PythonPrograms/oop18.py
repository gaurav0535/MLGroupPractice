class Base(object):
	def __init__(self):
		self.x = 10; self.y = 20;
	def calcBase(self):
		print "calc of base Executed"
	def displayBase(self):
		print "Display of Base Executed",self.x,self.y
		
class Derived(Base)
	def __init__(self):
		Base.__init__(self)
		self.a=100;self.b=200
	def calcDerived(self):
		print "calc of Derived Executed"
	def displayDerived(self):
		print "display of Derived Executed",self.a,self.b

ob = Derived()
ob.calcBase()
ob.calcDerived()

print "handle of calc derived', ob.c 
		