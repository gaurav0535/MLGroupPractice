class First :
	class_member = 0;
	def display (self):
		print self.class_member , First.class_member

ob1 = First()
ob2 = First()

ob1.class_member = 10
ob2.class_member = 20

First.class_member = 100

print " the value of member is " , First.class_member
ob1.display()
ob2.display()

First.class_member = 200

print " the value of member is", First.class_member
ob1.display()
ob2.display()
