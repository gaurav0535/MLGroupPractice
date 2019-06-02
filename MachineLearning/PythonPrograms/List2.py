listValue=[10,'one',20,'two',30,'three',40,'four',50,'five']
print " the given values of the list " , listValue
X = listValue.index(30)
print " the value given value 30 is present in %d index position" % X
y = listValue.pop()
print "The value Popped out of the list is " , y

print "Tje new values of the list is", listValue
listValue.remove(10)
print "The new value of the list " , listValue
listValue.sort()
print "The Sorted values of the list " , listValue
listValue.reverse()
print "The reverse  of the list " , listValue
listValue.insert(0,10)
print "the new list values of list is", listValue
print " THANK YOU"