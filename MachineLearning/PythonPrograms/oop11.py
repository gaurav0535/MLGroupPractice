class First:
	@classmethod
	def displayFirst(self) :
		print "Display of First Executed"
class Second(First):
	@classmethod
	def displaySecond(self):
		print "Display of Second Executed"
class Third(First):
	@classmethod
	def displayThird(self) :
		print "display of third Executed"
class Fourth(Second,Third) :
	@classmethod
	def displayFourth(self):
		print "Display of Fourth Executed"
		

		
ob = Fourth()
ob.displayFourth()
ob.displayThird()
ob.displaySecond()
ob.displayFirst()
