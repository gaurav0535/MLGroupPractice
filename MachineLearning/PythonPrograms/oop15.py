class Base:
	def calc(self):
		print "Calc of base executed"
	def display(self):
		print "display of base executed"
		
		
class Derived(Base):
	def calc(self):
		print "Calc of derived executed"
	def display(self):
		print "Display of Derived executed"

ob1= Base()
ob2 = Derived()
ob3= ob1
ob3.calc()
ob3.display()
ob3=ob2
ob3.calc()
ob3.display()