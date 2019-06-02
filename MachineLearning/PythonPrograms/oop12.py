class Base:
	def calc(self):
		print "Calc of Base Executed"
	def display(self):
		print "Display of Base Exected"
	
class Derived(Base):
	def calc(self):
		print "Calc of Derived Exected"
	def display(self):
		print "Display of Derived executed"
		
ob = Derived()
ob.calc()
ob.display()