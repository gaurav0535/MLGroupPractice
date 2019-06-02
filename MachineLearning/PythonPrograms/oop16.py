class Base:
	def __init__(self):
		print "Base class constructor executed",self
	def calcBase(self):
		print "Calc of Base Executed"
	def displayBase(self):
		print "display of base executed"
class Derived(Base):
	def __init__(self):
		print "Derived class constructor executed", self
	def calcDerived(self):
		print "calc Of derived executed"
	def displayDerived(self):
		print "Display of derived executed"
		
ob = Derived()
ob.calcDerived()
ob.calcBase()
ob.displayDerived()
ob.displayBase()
