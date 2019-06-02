#sample file handling

try :
	fd = open ('wipro.txt','r')
	count = 1
	print ' the file handle is : ', fd
	for x in fd:
		print count, ')',x
		count+=1
except IOError, e:
	print ' the file you are trying to open does not exist'
	print 'error :',e
except Exception,e:
	print 'Error occurred :' , e
else:
	fd.close()