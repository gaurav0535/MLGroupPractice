class Base:
    res=10
	def calc():
		Base.res+=10
		print "Calc is executed", Base.res
	def display():
		print "display of base executed"
	calc = staticmethod(calc)
	display = staticmethod(display)
print 'Class reference:', Base
print "Method reference: " , Base.calc,Base.display
Base.calc() 
base.display()

print " Contents of Base is : ", dir(Base)
print "Dictionary contents is : ", Base.__dict__
print "Contents :", dir()