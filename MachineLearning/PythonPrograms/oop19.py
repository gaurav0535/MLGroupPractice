class Base(object):
	@classmethod
	def __init__(self):
		self.X = 10;self.Y=20;
	@classmethod
	def displayBase(self):
		print "display of base executed",self.X,self.Y

class Derived(Base):
	@classmethod
	def __init__(self):
		super(Derived,self).__init__()
		self.a=100;self.b=200;
	@classmethod
	def displayDerived(self):
		print "display of derived Executed",self.a,self.b
		
ob = Derived()
ob.displayBase()
ob.displayDerived()
print 'the object information', dir(ob)

