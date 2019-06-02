class First :
	class_member = 0
	
ob1 = First()
ob2 = First()

ob1.class_member = 10
ob2.class_member = 20

print "the value of the member in OB1 is" , ob1.class_member
print "the value of the member in OB2 is" , ob2.class_member
print "The value of the member is", First.class_member
