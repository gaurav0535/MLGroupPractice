class First(object):
	class_member =10
	
class Second (First):
	pass
	
class Third(First):
	class_member = 20
	
class Fourth(Second,Third) :
	pass

ob = Fourth()
print ' Value of class_member:', ob.class_member