class First(object):
	def __init__(self):
		print ' The constructor of class first executed'
		self.x1 =1;self.y1=2;
class Second(First):
	def __init__(self):
		super(Second,self).__init__()
		print ' The constructor of class second executed'
		self.x2=10;self.y2=20;
class Third(Second):
	def __init__(self):
		super(Third,self).__init__()
		print ' the constructor of class Third Executed'
		self.x3=100;self.y3=200;
		
ob = Third()

print 'Member of OB of first', ob.x1,ob.y1
print 'Member of OB of second', ob.x2,ob.y2
print 'Member of OB of Third', ob.x3,ob.y3
