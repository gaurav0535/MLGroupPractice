class First:
	def First(self) :
		print 'Executing First'
class Second:
	def Second(self):
		print 'Executing Second'
		
class Third(First,Second) :
	def Third(self) :
		print 'Executing Third'
		
ob=Third()
ob.First()
ob.Second()
ob.Third()
		