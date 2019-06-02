listValue=[10,'one',20,'two',30,'three',40,'four',50,'five']
listValue1=['a','b','c','d','e']
print " the given values of the list is " , listValue
print " the length of given list is " , len(listValue)

listValue.append(60)
print " the Modified values of the list is " , listValue
x= listValue.count(10)
listValue[1]= 'one'

print "The values occurred %d  times :" % x
print "the values of the given list is ", len(listValue)
listValue.extend(listValue1)
print " the enxtended values of the list is " , listValue
print " the length of given list is " , len(listValue)
del(listValue[5])
print " the value at 4,5,6 index : listval"