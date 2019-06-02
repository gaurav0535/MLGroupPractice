class Base:
	def calcBase(self):
		print "Calc of base Executed"
	def displayBase(self):
		print "Display of Base Executed"
		
class Derived(Base):
	def calcDerived(self):
		print "calc of Derived Executed"
	def displayDerived(self):
		print "Display Derived Executed"
		
ob = Derived()
ob.calcDerived()
ob.displayDerived()

ob.calcBase()
ob.displayBase()