class First:
	def displayFirst(self):
		print "display of First Executed"
		
class Second(First) :
	def displaySecond(self):
		print " Display of Second executed"
		
class Third(Second):
	def displayThird(self):
		print "disp;au of third Executed"
		
ob= Third()
ob.displayThird()
ob.displaySecond()
ob.displayFirst()
