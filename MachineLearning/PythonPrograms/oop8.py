class sample :
    def first() :
	print ' I am a static method and I have executed'
	def second(self) :
	        print ' I am a class method and I have executed'
	first=staticmethod(first)
	second=staticmethod(second)
	
print 'Handle information of a class sample is \n, sample.__dict__

sample.first()
ob=sample()
ob.second()
