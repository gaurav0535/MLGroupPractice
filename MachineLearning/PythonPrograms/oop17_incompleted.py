class Base():
	def __init__(self):
		self.x = 0;self.y=0;
		print 'I am constructor of BAse'
	def calcBase(self) :
		print "calc of base executed"
	def displayBase(self):
		print "display of base execute",self.x,self.y
		
class Derived(Base):
	def __init__(self):
		self.a = 0;self.b = 0;
		print 'I am constructor of derived'
	def calcDerived(self):
		print 'Calc of derived execured