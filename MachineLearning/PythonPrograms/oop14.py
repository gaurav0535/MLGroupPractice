class Base:
	def calc(self):
		print "Calc of Base executed"
	def display(self):
		print "Display of Base Executed"
class Derived(Base):
	def calc(self):
		Base.calc(self)
		print "Calc of derived Executed"
	def display(self):
		Base.display(self)
		print "Display of Derived executed"

ob=Derived()
ob.calc()
ob.display()
