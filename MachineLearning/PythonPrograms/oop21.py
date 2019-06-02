class Base(object):
	@classmethod
	def calc(self):
		print "Calc of base executed"
	@classmethod
	def display(self):
		print "Display of base executed"
		
class Derived(Base):
	@classmethod
	def calc(self):
		super(Derived,self).calc()
		print "Calc of Derived executed"
	@classmethod
	def display(self):
		super(Derived,self).display()
		print "Display of Derived executed"
		
ob = Derived()
ob.calc()
ob.display()